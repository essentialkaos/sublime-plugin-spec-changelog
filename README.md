## Spec Changelog Plugin

Simple plugin for Sublime Text 3/4 for adding changelog record header.

### Installation

#### macOS

Open `Terminal.app` and do:

```bash
curl -OL# https://raw.githubusercontent.com/essentialkaos/sublime-plugin-spec-changelog/refs/heads/master/add_change_date.py
mv add_change_date.py "$HOME/Library/Application Support/Sublime Text/Packages/User/"
```

#### Windows

Press <kbd>Win</kbd>+<kbd>R</kbd>, type `powershell` and press Enter. Then do:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/essentialkaos/sublime-plugin-spec-changelog/refs/heads/master/add_change_date.py" -OutFile add_change_date.py
Move-Item -Force -Path add_change_date.py -Destination "$HOME\AppData\Roaming\Sublime Text\Packages\User\"
```

### Configuration

1. Go to _Preferences_ → _Settings_;
2. Add `spec_author_name` and `spec_author_mail` properties;
3. Go to _Preferences_ → _Key Bindings_;
4. Add something like this:
```json
[
  {"keys": ["ctrl+0"], "command": "prompt_add_change_date" }
]
```
5. Press <kbd>Ctrl</kbd>+<kbd>0</kbd> in your changelog section.

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://kaos.dev"><img src="https://raw.githubusercontent.com/essentialkaos/.github/refs/heads/master/images/ekgh.svg"/></a></p>
