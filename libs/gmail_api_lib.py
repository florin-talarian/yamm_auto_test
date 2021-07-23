"""
Created on Jun 25, 2021

@author: flba
"""

import pickle
import os
import base64
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.auth.exceptions import RefreshError


class GMailApi():

    def __init__(self):
        scopes = ["https://mail.google.com/",
                  "https://www.googleapis.com/auth/gmail.compose"]
        self.create_service("data/client_secret_file.json", "gmail", "v1", scopes)

    def create_service(self, client_secret_file, api_name, api_version, *scopes):
        scopes = [scope for scope in scopes[0]]
        cred = None
        pickle_file = f"token_{api_name}_{api_version}.pickle"
        if os.path.exists(pickle_file):
            with open(pickle_file, "rb") as token:
                cred = pickle.load(token)
        if not cred or not cred.valid:
            try:
                cred.refresh(Request())
            except RefreshError:
                flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
                cred = flow.run_local_server()
            with open(pickle_file, "wb") as token:
                pickle.dump(cred, token)
        try:
            self.service = build(api_name, api_version, credentials=cred)
        except Exception as exception:
            print("Unable to connect.")
            raise exception

    def create_message(self, sender, to, subject, message_text):
        self.message = MIMEMultipart()
        self.message["From"] = sender
        self.message["To"] = to
        self.message["Subject"] = subject
        self.message.attach(MIMEText(message_text, "plain"))

    def add_additional_message_subject(self, message, message_format):
        self.message.attach(MIMEText(message, message_format))

    def save_draft(self):
        raw_string = base64.urlsafe_b64encode(self.message.as_bytes()).decode()
        message = {"message": {"raw": raw_string}}
        return self.service.users().drafts().create(userId="me", body=message).execute()["id"]

    def delete_draft(self, draft_id):
        self.service.users().drafts().delete(userId="me", id=draft_id).execute()

    def list_messages(self, query):
        return self.service.users().messages().list(userId="me", q=query).execute()

    def get_message(self, msg_id):
        return self.service.users().messages().get(userId="me", id=msg_id).execute()
