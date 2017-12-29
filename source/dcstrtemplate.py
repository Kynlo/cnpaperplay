# !/usr/bin/python

# dcstrtemplate.py
# version 2.0, 10/14/17
# (c) mouser@donationcoder.com

"""
pdf helper object class
"""


class DcStrTemplate:
    """
    helper class for handling string templating
    """

    def __init__(self):
        self.text = '';
        self.fields = dict()

    def setText(self, text):
        self.text = text

    def loadFromFile(self, filepath):
        """Load file into text."""
        # open file and read contents
        with open(filepath, 'r') as myfile:
            self.text=myfile.read()
        #self.text = self.text.strip()


    def setField(self, fieldname, fieldval):
        self.fields[fieldname]=fieldval

    def retrieveText(self):
        """Replace all fields in text and return it."""
        str = self.text
        for k,v in self.fields.items():
            str = str.replace(k,v)
        return str

    def getField(self, fieldname, defaultval = ''):
        if fieldname in self.fields:
            return self.fields[fieldname]
        return defaultval