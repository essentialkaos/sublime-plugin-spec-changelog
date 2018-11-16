import datetime
import sublime, sublime_plugin

class PromptAddChangeDateCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.show_input_panel("Version:", "", self.on_done, None, None)

  def on_done(self, text):
    if self.window.active_view():
      self.window.active_view().run_command("add_change_date", {"version": text})

class AddChangeDateCommand(sublime_plugin.TextCommand):
  def run(self, edit, version):
    author_name = "User"
    author_mail = "mail@domain.com"

    settings = sublime.load_settings("Preferences.sublime-settings")

    if settings.has("spec_author_name"):
      author_name = settings.get("spec_author_name")
    if settings.has("spec_author_mail"):
      author_mail = settings.get("spec_author_mail")

    date = datetime.date.today().strftime("%a %b %d %Y")
    
    self.view.run_command("insert_snippet", {"contents": "* %s %s <%s> - %s\n- " % (date, author_name, author_mail, version)})
