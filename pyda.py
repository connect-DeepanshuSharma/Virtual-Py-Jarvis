import wolframalpha
import wikipedia
import wx
import pyttsx
import speech_recognition as sr

#while True:
#    question= raw_input("\nQuestion:")

#GUI
engine = pyttsx.init()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Pyda the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        question = self.txt.GetValue()
        question  = question.lower()
        if question == ' ':
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                print("You said: " + r.recognize_google(audio))
            except sr.UnknownValueError:
                print "Google Speech Recognition could not understand audio"
            except sr.RequestError as e:
                print "Could not request results from Google Speech Recognition service; {0}".format(e)

        else
            try:
                wolframalpha
                app_id = "3QW4X2-H62XWXHH2J"  #app_id of wolframalpha after signing up
                client = wolframalpha.Client(app_id) #calling client using app_id
                result = client.query(question)
                answer = next(result.results).text
                print (answer)
                engine.say(question)
                engine.runAndWait()
                engine.say(question + "is :" + answer)
                engine.runAndWait()

            except:
                wikipedia
                #wikipedia.set_lang("eng")
                question= question.split(" ")
                question = " ".join(question[2:])
                engine.say("Searched for" + question)
                engine.runAndWait()
                print wikipedia.summary(question)


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
