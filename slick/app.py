#!/usr/bin/env python

import toga


class Slick(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.main_window.app = self

        self.webview = toga.WebView()

        self.main_window.content = self.webview

        self.webview.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8"
        self.webview.url = "https://djangoconus2017.slack.com/messages"

        self.main_window.show()

    def load_page(self, widget):
        self.webview.url = self.url_input.value

def main():
    return Slick('Slick', 'org.pybee.slick')
