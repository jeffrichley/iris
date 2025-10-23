Directory structure:
└── textualize-textual/
    ├── README.md
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── docs.md
    ├── faq.yml
    ├── LICENSE
    ├── Makefile
    ├── mkdocs-common.yml
    ├── mkdocs-nav.yml
    ├── mkdocs-offline.yml
    ├── mkdocs-online.yml
    ├── mypy.ini
    ├── pyproject.toml
    ├── .coveragerc
    ├── .deepsource.toml
    ├── .pre-commit-config.yaml
    ├── docs/
    │   ├── CNAME
    │   ├── FAQ.md
    │   ├── getting_started.md
    │   ├── help.md
    │   ├── index.md
    │   ├── roadmap.md
    │   ├── robots.txt
    │   ├── tutorial.md
    │   ├── widget_gallery.md
    │   ├── api/
    │   │   ├── app.md
    │   │   ├── await_complete.md
    │   │   ├── await_remove.md
    │   │   ├── binding.md
    │   │   ├── cache.md
    │   │   ├── color.md
    │   │   ├── command.md
    │   │   ├── compose.md
    │   │   ├── constants.md
    │   │   ├── containers.md
    │   │   ├── content.md
    │   │   ├── coordinate.md
    │   │   ├── dom_node.md
    │   │   ├── errors.md
    │   │   ├── events.md
    │   │   ├── filter.md
    │   │   ├── fuzzy_matcher.md
    │   │   ├── geometry.md
    │   │   ├── getters.md
    │   │   ├── highlight.md
    │   │   ├── index.md
    │   │   ├── layout.md
    │   │   ├── lazy.md
    │   │   ├── logger.md
    │   │   ├── logging.md
    │   │   ├── map_geometry.md
    │   │   ├── markup.md
    │   │   ├── message.md
    │   │   ├── message_pump.md
    │   │   ├── on.md
    │   │   ├── pilot.md
    │   │   ├── query.md
    │   │   ├── reactive.md
    │   │   ├── renderables.md
    │   │   ├── screen.md
    │   │   ├── scroll_view.md
    │   │   ├── scrollbar.md
    │   │   ├── signal.md
    │   │   ├── strip.md
    │   │   ├── style.md
    │   │   ├── suggester.md
    │   │   ├── system_commands_source.md
    │   │   ├── timer.md
    │   │   ├── types.md
    │   │   ├── validation.md
    │   │   ├── walk.md
    │   │   ├── widget.md
    │   │   ├── work.md
    │   │   ├── worker.md
    │   │   └── worker_manager.md
    │   ├── blog/
    │   │   ├── index.md
    │   │   ├── .authors.yml
    │   │   └── posts/
    │   │       ├── anatomy-of-a-textual-user-interface.md
    │   │       ├── await-me-maybe.md
    │   │       ├── be-the-keymaster.md
    │   │       ├── better-sleep-on-windows.md
    │   │       ├── create-task-psa.md
    │   │       ├── creating-tasks-overhead.md
    │   │       ├── darren-year-in-review.md
    │   │       ├── future-of-textualize.md
    │   │       ├── helo-world.md
    │   │       ├── inline-mode.md
    │   │       ├── looking-for-help.md
    │   │       ├── on-dog-food-the-original-metaverse-and-not-being-bored.md
    │   │       ├── placeholder-pr.md
    │   │       ├── puppies-and-cake.md
    │   │       ├── release0-11-0.md
    │   │       ├── release0-12-0.md
    │   │       ├── release0-14-0.md
    │   │       ├── release0-15-0.md
    │   │       ├── release0-16-0.md
    │   │       ├── release0-17-0.md
    │   │       ├── release0-18-0.md
    │   │       ├── release0-23-0.md
    │   │       ├── release0-24-0.md
    │   │       ├── release0-27-0.md
    │   │       ├── release0-29-0.md
    │   │       ├── release0-30-0.md
    │   │       ├── release0-38-0.md
    │   │       ├── release0-4-0.md
    │   │       ├── release0-6-0.md
    │   │       ├── release0.37.0.md
    │   │       ├── release1.0.0.md
    │   │       ├── remote-memray.md
    │   │       ├── responsive-app-background-task.md
    │   │       ├── rich-inspect.md
    │   │       ├── smooth-scrolling.md
    │   │       ├── spinners-and-pbs-in-textual.md
    │   │       ├── steal-this-code.md
    │   │       ├── text-area-learnings.md
    │   │       ├── textual-plotext.md
    │   │       ├── textual-serve-files.md
    │   │       ├── textual-web.md
    │   │       ├── to-tui-or-not-to-tui.md
    │   │       └── toolong-retrospective.md
    │   ├── css_types/
    │   │   ├── _template.md
    │   │   ├── border.md
    │   │   ├── color.md
    │   │   ├── hatch.md
    │   │   ├── horizontal.md
    │   │   ├── index.md
    │   │   ├── integer.md
    │   │   ├── keyline.md
    │   │   ├── name.md
    │   │   ├── number.md
    │   │   ├── overflow.md
    │   │   ├── percentage.md
    │   │   ├── position.md
    │   │   ├── scalar.md
    │   │   ├── text_align.md
    │   │   ├── text_style.md
    │   │   └── vertical.md
    │   ├── custom_theme/
    │   │   └── main.html
    │   ├── events/
    │   │   ├── app_blur.md
    │   │   ├── app_focus.md
    │   │   ├── blur.md
    │   │   ├── click.md
    │   │   ├── descendant_blur.md
    │   │   ├── descendant_focus.md
    │   │   ├── enter.md
    │   │   ├── focus.md
    │   │   ├── hide.md
    │   │   ├── index.md
    │   │   ├── key.md
    │   │   ├── leave.md
    │   │   ├── load.md
    │   │   ├── mount.md
    │   │   ├── mouse_capture.md
    │   │   ├── mouse_down.md
    │   │   ├── mouse_move.md
    │   │   ├── mouse_release.md
    │   │   ├── mouse_scroll_down.md
    │   │   ├── mouse_scroll_left.md
    │   │   ├── mouse_scroll_right.md
    │   │   ├── mouse_scroll_up.md
    │   │   ├── mouse_up.md
    │   │   ├── paste.md
    │   │   ├── print.md
    │   │   ├── resize.md
    │   │   ├── screen_resume.md
    │   │   ├── screen_suspend.md
    │   │   ├── show.md
    │   │   └── unmount.md
    │   ├── examples/
    │   │   ├── styles/
    │   │   │   └── README.md
    │   │   └── widgets/
    │   │       └── java_highlights.scm
    │   ├── guide/
    │   │   ├── actions.md
    │   │   ├── animation.md
    │   │   ├── app.md
    │   │   ├── command_palette.md
    │   │   ├── content.md
    │   │   ├── CSS.md
    │   │   ├── design.md
    │   │   ├── devtools.md
    │   │   ├── events.md
    │   │   ├── index.md
    │   │   ├── input.md
    │   │   ├── layout.md
    │   │   ├── queries.md
    │   │   ├── reactivity.md
    │   │   ├── screens.md
    │   │   ├── styles.md
    │   │   ├── testing.md
    │   │   ├── widgets.md
    │   │   └── workers.md
    │   ├── how-to/
    │   │   ├── center-things.md
    │   │   ├── design-a-layout.md
    │   │   ├── index.md
    │   │   ├── package-with-hatch.md
    │   │   ├── render-and-compose.md
    │   │   ├── style-inline-apps.md
    │   │   └── work-with-containers.md
    │   ├── reference/
    │   │   └── index.md
    │   ├── snippets/
    │   │   ├── border_sub_title_align_all_example.md
    │   │   ├── border_title_color.md
    │   │   ├── border_vs_outline_example.md
    │   │   ├── see_also_border.md
    │   │   ├── syntax_block_end.md
    │   │   └── syntax_block_start.md
    │   ├── styles/
    │   │   ├── _template.md
    │   │   ├── align.md
    │   │   ├── background.md
    │   │   ├── background_tint.md
    │   │   ├── border.md
    │   │   ├── border_subtitle_align.md
    │   │   ├── border_subtitle_background.md
    │   │   ├── border_subtitle_color.md
    │   │   ├── border_subtitle_style.md
    │   │   ├── border_title_align.md
    │   │   ├── border_title_background.md
    │   │   ├── border_title_color.md
    │   │   ├── border_title_style.md
    │   │   ├── box_sizing.md
    │   │   ├── color.md
    │   │   ├── content_align.md
    │   │   ├── display.md
    │   │   ├── dock.md
    │   │   ├── hatch.md
    │   │   ├── height.md
    │   │   ├── index.md
    │   │   ├── keyline.md
    │   │   ├── layer.md
    │   │   ├── layers.md
    │   │   ├── layout.md
    │   │   ├── margin.md
    │   │   ├── max_height.md
    │   │   ├── max_width.md
    │   │   ├── min_height.md
    │   │   ├── min_width.md
    │   │   ├── offset.md
    │   │   ├── opacity.md
    │   │   ├── outline.md
    │   │   ├── overflow.md
    │   │   ├── padding.md
    │   │   ├── position.md
    │   │   ├── scrollbar_gutter.md
    │   │   ├── scrollbar_size.md
    │   │   ├── scrollbar_visibility.md
    │   │   ├── text_align.md
    │   │   ├── text_opacity.md
    │   │   ├── text_overflow.md
    │   │   ├── text_style.md
    │   │   ├── text_wrap.md
    │   │   ├── tint.md
    │   │   ├── visibility.md
    │   │   ├── width.md
    │   │   ├── grid/
    │   │   │   ├── column_span.md
    │   │   │   ├── grid_columns.md
    │   │   │   ├── grid_gutter.md
    │   │   │   ├── grid_rows.md
    │   │   │   ├── grid_size.md
    │   │   │   ├── index.md
    │   │   │   └── row_span.md
    │   │   ├── links/
    │   │   │   ├── index.md
    │   │   │   ├── link_background.md
    │   │   │   ├── link_background_hover.md
    │   │   │   ├── link_color.md
    │   │   │   ├── link_color_hover.md
    │   │   │   ├── link_style.md
    │   │   │   └── link_style_hover.md
    │   │   └── scrollbar_colors/
    │   │       ├── index.md
    │   │       ├── scrollbar_background.md
    │   │       ├── scrollbar_background_active.md
    │   │       ├── scrollbar_background_hover.md
    │   │       ├── scrollbar_color.md
    │   │       ├── scrollbar_color_active.md
    │   │       ├── scrollbar_color_hover.md
    │   │       └── scrollbar_corner_color.md
    │   ├── stylesheets/
    │   │   └── custom.css
    │   └── widgets/
    │       ├── _template.md
    │       ├── button.md
    │       ├── checkbox.md
    │       ├── collapsible.md
    │       ├── content_switcher.md
    │       ├── data_table.md
    │       ├── digits.md
    │       ├── directory_tree.md
    │       ├── footer.md
    │       ├── header.md
    │       ├── index.md
    │       ├── input.md
    │       ├── label.md
    │       ├── link.md
    │       ├── list_item.md
    │       ├── list_view.md
    │       ├── loading_indicator.md
    │       ├── log.md
    │       ├── markdown.md
    │       ├── markdown_viewer.md
    │       ├── masked_input.md
    │       ├── option_list.md
    │       ├── placeholder.md
    │       ├── pretty.md
    │       ├── progress_bar.md
    │       ├── radiobutton.md
    │       ├── radioset.md
    │       ├── rich_log.md
    │       ├── rule.md
    │       ├── select.md
    │       ├── selection_list.md
    │       ├── sparkline.md
    │       ├── static.md
    │       ├── switch.md
    │       ├── tabbed_content.md
    │       ├── tabs.md
    │       ├── text_area.md
    │       ├── toast.md
    │       └── tree.md
    ├── examples/
    │   ├── README.md
    │   ├── demo.md
    │   ├── example.md
    │   └── five_by_five.md
    ├── notes/
    │   ├── README.md
    │   ├── refresh.md
    │   └── snapshot_testing.md
    ├── questions/
    │   ├── README.md
    │   ├── align-center-middle.question.md
    │   ├── compose-result.question.md
    │   ├── copy-text.question.md
    │   ├── images.question.md
    │   ├── pass-args-to-app.question.md
    │   ├── transparent-background.question.md
    │   ├── why-do-some-keys-not-make-it-to-my-app.question.md
    │   ├── why-looks-bad-on-macos.question.md
    │   ├── why-no-ansi-themes.question.md
    │   └── worker-thread-error.question.md
    ├── reference/
    │   ├── README.md
    │   ├── box.monopic
    │   └── spacing.monopic
    ├── src/
    │   └── textual/
    │       ├── py.typed
    │       ├── tree-sitter/
    │       │   └── highlights/
    │       │       ├── bash.scm
    │       │       ├── css.scm
    │       │       ├── go.scm
    │       │       ├── html.scm
    │       │       ├── java.scm
    │       │       ├── javascript.scm
    │       │       ├── json.scm
    │       │       ├── markdown.scm
    │       │       ├── python.scm
    │       │       ├── regex.scm
    │       │       ├── rust.scm
    │       │       ├── sql.scm
    │       │       ├── toml.scm
    │       │       ├── xml.scm
    │       │       └── yaml.scm
    │       └── widgets/
    │           └── __init__.pyi
    ├── tests/
    │   └── snapshot_tests/
    │       └── snapshot_report_template.jinja2
    ├── tools/
    │   └── gen_easings_tests.ts
    ├── .faq/
    │   ├── FAQ.md
    │   └── suggest.md
    └── .github/
        ├── FUNDING.yml
        ├── PULL_REQUEST_TEMPLATE.md
        ├── ISSUE_TEMPLATE/
        │   ├── bug_report.md
        │   └── config.yml
        └── workflows/
            ├── black_format.yml
            ├── codeql.yml
            ├── comment.yml
            ├── new_issue.yml
            └── pythonpackage.yml


Files Content:

(Files content cropped to 300k characters, download full ingest to see more)
================================================
FILE: README.md
================================================


[![Discord](https://img.shields.io/discord/1026214085173461072)](https://discord.gg/Enf6Z3qhVr)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/textual)](https://pypi.org/project/textual/)
[![PyPI version](https://badge.fury.io/py/textual.svg?)](https://badge.fury.io/py/textual)
![OS support](https://img.shields.io/badge/OS-macOS%20Linux%20Windows-red)



![textual-splash](https://github.com/user-attachments/assets/4caeb77e-48c0-4cf7-b14d-c53ded855ffd)

# Textual

<img align="right" width="250" alt="clock" src="https://github.com/user-attachments/assets/63e839c3-5b8e-478d-b78e-cf7647eb85e8" />

Build cross-platform user interfaces with a simple Python API. Run your apps in the terminal *or* a web browser.

Textual's API combines modern Python with the best of developments from the web world, for a lean app development experience.
De-coupled components and an advanced [testing](https://textual.textualize.io/guide/testing/) framework ensure you can maintain your app for the long-term.

Want some more examples? See the [examples](https://github.com/Textualize/textual/tree/main/examples) directory.

```python
"""
An App to show the current time.
"""

from datetime import datetime

from textual.app import App, ComposeResult
from textual.widgets import Digits


class ClockApp(App):
    CSS = """
    Screen { align: center middle; }
    Digits { width: auto; }
    """

    def compose(self) -> ComposeResult:
        yield Digits("")

    def on_ready(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = datetime.now().time()
        self.query_one(Digits).update(f"{clock:%T}")


if __name__ == "__main__":
    app = ClockApp()
    app.run()
```

> [!TIP]
> Textual is an asynchronous framework under the hood. Which means you can integrate your apps with async libraries &mdash; if you want to.
> If you don't want or need to use async, Textual won't force it on you.



<img src="https://img.spacergif.org/spacer.gif" width="1" height="64"/>

## Widgets

Textual's library of [widgets](https://textual.textualize.io/widget_gallery/) covers everything from buttons, tree controls, data tables, inputs, text areas, and more…
Combined with a flexible [layout](https://textual.textualize.io/how-to/design-a-layout/) system, you can realize any User Interface you need.

Predefined themes ensure your apps will look good out of the box.


<table>

<tr>

  <td>

  ![buttons](https://github.com/user-attachments/assets/2ac26387-aaa3-41ed-bc00-7d488600343c)

  </td>

  <td>

![tree](https://github.com/user-attachments/assets/61ccd6e9-97ea-4918-8eda-3ee0f0d3770e)

  </td>

</tr>


<tr>

  <td>

  ![datatables](https://github.com/user-attachments/assets/3e1f9f7a-f965-4901-a114-3c188bd17695)

  </td>

  <td>

![inputs](https://github.com/user-attachments/assets/b02aa203-7c37-42da-a1bb-2cb244b7d0d3)

  </td>

</tr>
<tr>

<td>

![listview](https://github.com/user-attachments/assets/963603bc-aa07-4688-bd24-379962ece871)

</td>

<td>

![textarea](https://github.com/user-attachments/assets/cd4ba787-5519-40e2-8d86-8224e1b7e506)

</td>


</tr>

</table>


<img src="https://img.spacergif.org/spacer.gif" width="1" height="32"/>

## Installing

Install Textual via pip:

```
pip install textual textual-dev
```

See [getting started](https://textual.textualize.io/getting_started/) for details.


<img src="https://img.spacergif.org/spacer.gif" width="1" height="32"/>

## Demo


Run the following command to see a little of what Textual can do:

```
python -m textual
```

Or try the [textual demo](https://github.com/textualize/textual-demo) *without* installing (requires [uv](https://docs.astral.sh/uv/)):

```bash
uvx --python 3.12 textual-demo
```

<img src="https://img.spacergif.org/spacer.gif" width="1" height="32"/>

## Dev Console

<img align="right" width="40%" alt="devtools" src="https://github.com/user-attachments/assets/12c60d65-e342-4b2f-9372-bae0459a7552" />


How do you debug an app in the terminal that is also running in the terminal?

The `textual-dev` package supplies a dev console that connects to your application from another terminal.
In addition to system messages and events, your logged messages and print statements will appear in the dev console.

See [the guide](https://textual.textualize.io/guide/devtools/) for other helpful tools provided by the `textual-dev` package.

<img src="https://img.spacergif.org/spacer.gif" width="1" height="32"/>

## Command Palette


Textual apps have a *fuzzy search* command palette.
Hit `ctrl+p` to open the command palette.

It is easy to extend the command palette with [custom commands](https://textual.textualize.io/guide/command_palette/) for your application.


![Command Palette](https://github.com/user-attachments/assets/94d8ec5d-b668-4033-a5cb-bf820e1b8d60)

<img src="https://img.spacergif.org/spacer.gif" width="1" height="32"/>

# Textual ❤️ Web

<img align="right" width="40%" alt="textual-serve" src="https://github.com/user-attachments/assets/a25820fb-87ae-433a-858b-ac3940169242">


Textual apps are equally at home in the browser as they are the terminal. Any Textual app may be served with `textual serve` &mdash; so you can share your creations on the web.
Here's how to serve the demo app:

```
textual serve "python -m textual"
```

In addition to serving your apps locally, you can serve apps with [Textual Web](https://github.com/Textualize/textual-web).

Textual Web's firewall-busting technology can serve an unlimited number of applications.

Since Textual apps have low system requirements, you can install them anywhere Python also runs. Turning any device into a connected device.
No desktop required!


<img src="https://img.spacergif.org/spacer.gif" width="1" height="32"/>


## Join us on Discord

Join the Textual developers and community on our [Discord Server](https://discord.gg/Enf6Z3qhVr).



================================================
FILE: CODE_OF_CONDUCT.md
================================================
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
[will@textualize.io](mailto:will@textualize.io).
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.


================================================
FILE: CONTRIBUTING.md
================================================
# Contributing to Textual

First of all, thanks for taking the time to contribute to Textual!

## How can I contribute?

You can contribute to Textual in many ways:

 1. [Report a bug](https://github.com/textualize/textual/issues/new?title=%5BBUG%5D%20short%20bug%20description&template=bug_report.md)
 2. Add a new feature
 3. Fix a bug
 4. Improve the documentation


## Setup

To make a code or documentation contribution you will need to set up Textual locally.
You can follow these steps:

 1. Make sure you have Poetry installed ([see instructions here](https://python-poetry.org))
 2. Clone the Textual repository
 3. Run `poetry shell` to create a virtual environment for the dependencies
 4. Run `make setup` to install all dependencies
 5. Make sure the latest version of Textual was installed by running the command `textual --version`
 6. Install the pre-commit hooks with the command `pre-commit install`

([Read this](#makefile-commands) if the command `make` doesn't work for you.)

## Demo

Once you have Textual installed, run the Textual demo to get an impression of what Textual can do and to double check that everything was installed correctly:

```bash
python -m textual
```

## Guidelines

- Read any issue instructions carefully. Feel free to ask for clarification if any details are missing.

- Add docstrings to all of your code (functions, methods, classes, ...). The codebase should have enough examples for you to copy from.

- Write tests for your code.
  - If you are fixing a bug, make sure to add regression tests that link to the original issue.
  - If you are implementing a visual element, make sure to add _snapshot tests_. [See below](#snapshot-testing) for more details.

## Before opening a PR

Before you open your PR, please go through this checklist and make sure you've checked all the items that apply:

 - [ ] Update the `CHANGELOG.md`
 - [ ] Format your code with black (`make format`)
 - [ ] All your code has docstrings in the style of the rest of the codebase
 - [ ] Your code passes all tests (`make test`)

([Read this](#makefile-commands) if the command `make` doesn't work for you.)

## Updating and building the documentation

If you change the documentation, you will want to build the documentation to make sure everything looks like it should.
The command `make docs-serve-offline` should start a server that will let you preview the documentation locally and that should reload whenever you save changes to the documentation or the code files.

([Read this](#makefile-commands) if the command `make` doesn't work for you.)

We strive to write our documentation in a clear and accessible way so, if you find any issues with the documentation, we encourage you to open an issue where you can enumerate the things you think should be changed or added.

Opening an issue or a discussion is typically better than opening a PR directly.
That's because there are many subjective considerations that go into writing documentation and we cannot expect you, a well-intentioned external contributor, to be aware of those subjective considerations that we take into account when writing our documentation.

Of course, this does not apply to objective/technical issues with the documentation like bugs or broken links.

## After opening a PR

When you open a PR, your code will be reviewed by one of the Textual maintainers.
In that review process,

- We will take a look at all of the changes you are making
- We might ask for clarifications (why did you do X or Y?)
- We might ask for more tests/more documentation
- We might ask for some code changes

The sole purpose of those interactions is to make sure that, in the long run, everyone has the best experience possible with Textual and with the feature you are implementing/fixing.

Don't be discouraged if a reviewer asks for code changes.
If you go through our history of pull requests, you will see that every single one of the maintainers has had to make changes following a review.

## Snapshot testing

Snapshot tests ensure that visual things (like widgets) look like they are supposed to.
PR [#1969](https://github.com/Textualize/textual/pull/1969) is a good example of what adding snapshot tests looks like: it amounts to a change in the file `tests/snapshot_tests/test_snapshots.py` that should run an app that you write and compare it against a historic snapshot of what that app should look like.

When you create a new snapshot test, run it with `pytest -vv tests/snapshot_tests/test_snapshots.py`.
Because you just created this snapshot test, there is no history to compare against and the test will fail.
After running the snapshot tests, you should see a link that opens an interface in your browser.
This interface should show all failing snapshot tests and a side-by-side diff between what the app looked like when the test ran versus the historic snapshot.

Make sure your snapshot app looks like it is supposed to and that you didn't break any other snapshot tests.
If everything looks fine, you can run `make test-snapshot-update` to update the snapshot history with your new snapshot.
This will write a new SVG file to the `tests/snapshot_tests/__snapshots__/` directory.
You should NOT modify these files by hand.
If a pre-existing snapshot tests fails, you should carefully inspect the diff and decide if the new snapshot is correct or if the pre-existing one is.
If the new snapshot is correct, you should update the snapshot history with your new snapshot using `make test-snapshot-update`.
If the pre-existing snapshot is correct, your change has likely introduced a bug, and you should try to fix it.
After fixing it, and checking the output of `make test-snapshot` now looks correct, you should run `make test-snapshot-update` to update the snapshot history with your new snapshot.


([Read this](#makefile-commands) if the command `make` doesn't work for you.)

## Join the community

Seems a little overwhelming?
Join our community on [Discord](https://discord.gg/Enf6Z3qhVr) to get help!

## Makefile commands

Textual has a `Makefile` file that contains the most common commands used when developing Textual.
([Read about Make and makefiles on Wikipedia.](https://en.wikipedia.org/wiki/Make_(software)))
If you don't have Make and you're on Windows, you may want to [install Make](https://stackoverflow.com/q/32127524/2828287).



================================================
FILE: docs.md
================================================
# Documentation Workflow

* Ensure you're inside a *Python 3.10+* virtual environment
* Run the live-reload server using `mkdocs serve` from the project root
* Create new pages by adding new directories and Markdown files inside `docs/*`

## Commands

- `mkdocs serve` - Start the live-reloading docs server.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.



================================================
FILE: faq.yml
================================================
# FAQtory settings

faq_url: "https://textual.textualize.io/FAQ/" # Replace this with the URL to your FAQ.md!

questions_path: "./questions" # Where questions should be stored
output_path: "./docs/FAQ.md" # Where FAQ.md should be generated
templates_path: ".faq" # Path to templates



================================================
FILE: LICENSE
================================================
MIT License

Copyright (c) 2021 Will McGugan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



================================================
FILE: Makefile
================================================
run := poetry run

.PHONY: test
test:
	$(run) pytest tests/ -n 16 --dist=loadgroup $(ARGS)

.PHONY: testv
testv:
	$(run) pytest tests/ -vvv -n 16 --dist=loadgroup $(ARGS)

.PHONY: test-snapshot-update
test-snapshot-update:
	$(run) pytest tests/ --snapshot-update -n 16 --dist=loadgroup $(ARGS)

.PHONY: test-coverage
test-coverage:
	$(run) pytest tests/ --cov-report term-missing --cov=textual -n 16 --dist=loadgroup $(ARGS)

.PHONY: coverage
coverage:
	$(run) coverage html

.PHONY: typecheck
typecheck:
	$(run) mypy src/textual

.PHONY: format
format:
	$(run) black src

.PHONY: format-check
format-check:
	$(run) black --check src

.PHONY: clean-screenshot-cache
clean-screenshot-cache:
	rm -rf .screenshot_cache

.PHONY: faq
faq:
	$(run) faqtory build

.PHONY: docs-offline-nav
docs-offline-nav:
	echo "INHERIT: mkdocs-offline.yml" > mkdocs-nav-offline.yml
	grep -v "\- \"*[Bb]log" mkdocs-nav.yml >> mkdocs-nav-offline.yml

.PHONY: docs-online-nav
docs-online-nav:
	echo "INHERIT: mkdocs-online.yml" > mkdocs-nav-online.yml
	cat mkdocs-nav.yml >> mkdocs-nav-online.yml

.PHONY: docs-serve
docs-serve: clean-screenshot-cache docs-online-nav
	TEXTUAL_THEME=dracula $(run) mkdocs serve --config-file mkdocs-nav-online.yml
	rm -f mkdocs-nav-online.yml

.PHONY: docs-serve-offline
docs-serve-offline: clean-screenshot-cache docs-offline-nav
	$(run) mkdocs serve --config-file mkdocs-nav-offline.yml
	rm -f mkdocs-nav-offline.yml

.PHONY: docs-build
docs-build: docs-online-nav
	$(run) mkdocs build --config-file mkdocs-nav-online.yml
	rm -f mkdocs-nav-online.yml

.PHONY: docs-build-offline
docs-build-offline: docs-offline-nav
	$(run) mkdocs build --config-file mkdocs-nav-offline.yml
	rm -f mkdocs-nav-offline.yml

.PHONY: clean-offline-docs
clean-offline-docs:
	rm -rf docs-offline

.PHONY: docs-deploy
docs-deploy: clean-screenshot-cache docs-online-nav
	TEXTUAL_THEME=dracula $(run) mkdocs gh-deploy --config-file mkdocs-nav-online.yml
	rm -f mkdocs-nav-online.yml

.PHONY: build
build: docs-build-offline
	poetry build

.PHONY: clean
clean: clean-screenshot-cache clean-offline-docs

.PHONY: setup
setup:
	poetry install
	poetry install --extras syntax

.PHONY: update
update:
	poetry update

.PHONY: install-pre-commit
install-pre-commit:
	$(run) pre-commit install

.PHONY: demo
demo:
	$(run) python -m textual

.PHONY: repl
repl:
	$(run) python



================================================
FILE: mkdocs-common.yml
================================================
site_name: Textual

markdown_extensions:
  - attr_list
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - md_in_html
  - admonition
  - def_list
  - meta
  - footnotes

  - toc:
      permalink: true
      baselevel: 1
  - pymdownx.keys
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.superfences:
      custom_fences:
        - name: textual
          class: textual
          format: !!python/name:textual._doc.format_svg
        - name: rich
          class: rich
          format: !!python/name:textual._doc.rich
  - pymdownx.inlinehilite
  - pymdownx.superfences
  - pymdownx.snippets
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.snippets
  - markdown.extensions.attr_list
  - pymdownx.details

theme:
  name: material
  custom_dir: docs/custom_theme
  logo: images/icons/logo light transparent.svg
  features:
    - navigation.tabs
    - navigation.indexes
    - navigation.tabs.sticky
    - navigation.footer
    - content.code.annotate
    - content.code.copy
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      accent: purple
      toggle:
        icon: material/weather-sunny
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: black
      toggle:
        icon: material/weather-night
        name: Switch to light mode

plugins:
  git-revision-date-localized:
  search:
  autorefs:
  mkdocstrings:
    default_handler: python
    handlers:
      python:
        options:
          modernize_annotations: false
          show_symbol_type_heading: true
          show_symbol_type_toc: true
          show_signature_annotations: false
          separate_signature: true
          signature_crossrefs: true
          merge_init_into_class: true
          parameter_headings: true
          show_root_heading: false
          docstring_options:
            ignore_init_summary: true
          show_source: false
          filters:
            - "!^_"
            - "^__init__$"
            - "!^can_replace$"
            # Hide some methods that Widget subclasses implement but that we don't want
            # to be shown in the docs.
            # This is then overridden in widget.md and app.md so that it shows in the
            # base class.
            - "!^compose$"
            - "!^render$"
            - "!^render_line$"
            - "!^render_lines$"
            - "!^get_content_width$"
            - "!^get_content_height$"
            - "!^compose_add_child$"
    watch:
      - mkdocs-common.yml
      - mkdocs-nav.yml
      - mkdocs-offline.yml
      - mkdocs-online.yml
      - src/textual
  exclude:
    glob:
      - "**/_template.md"
      - "snippets/*"

extra_css:
  - stylesheets/custom.css

extra:
  social:
    - icon: fontawesome/brands/twitter
      link: https://twitter.com/textualizeio
      name: textualizeio on Twitter
    - icon: fontawesome/brands/github
      link: https://github.com/textualize/textual/
      name: Textual on Github
    - icon: fontawesome/brands/discord
      link: https://discord.gg/Enf6Z3qhVr
      name: Textual Discord server
copyright: Copyright &copy; Textualize, Inc



================================================
FILE: mkdocs-nav.yml
================================================
nav:
  - "index.md"
  - Introduction:
      - "getting_started.md"
      - "help.md"
  - "tutorial.md"
  - Guide:
      - "guide/index.md"
      - "guide/devtools.md"
      - "guide/app.md"
      - "guide/styles.md"
      - "guide/CSS.md"
      - "guide/queries.md"
      - "guide/layout.md"
      - "guide/events.md"
      - "guide/input.md"
      - "guide/actions.md"
      - "guide/reactivity.md"
      - "guide/design.md"
      - "guide/widgets.md"
      - "guide/content.md"
      - "guide/animation.md"
      - "guide/screens.md"
      - "guide/workers.md"
      - "guide/command_palette.md"
      - "guide/testing.md"
  - "widget_gallery.md"
  - Reference:
      - "reference/index.md"
      - CSS Types:
          - "css_types/index.md"
          - "css_types/border.md"
          - "css_types/color.md"
          - "css_types/hatch.md"
          - "css_types/horizontal.md"
          - "css_types/integer.md"
          - "css_types/keyline.md"
          - "css_types/name.md"
          - "css_types/number.md"
          - "css_types/overflow.md"
          - "css_types/position.md"
          - "css_types/percentage.md"
          - "css_types/scalar.md"
          - "css_types/text_align.md"
          - "css_types/text_style.md"
          - "css_types/vertical.md"
      - Events:
          - "events/index.md"
          - "events/app_blur.md"
          - "events/app_focus.md"
          - "events/blur.md"
          - "events/click.md"
          - "events/descendant_blur.md"
          - "events/descendant_focus.md"
          - "events/enter.md"
          - "events/focus.md"
          - "events/hide.md"
          - "events/key.md"
          - "events/leave.md"
          - "events/load.md"
          - "events/mount.md"
          - "events/mouse_capture.md"
          - "events/mouse_down.md"
          - "events/mouse_move.md"
          - "events/mouse_release.md"
          - "events/mouse_scroll_down.md"
          - "events/mouse_scroll_up.md"
          - "events/mouse_up.md"
          - "events/paste.md"
          - "events/print.md"
          - "events/resize.md"
          - "events/screen_resume.md"
          - "events/screen_suspend.md"
          - "events/show.md"
          - "events/unmount.md"
      - Styles:
          - "styles/index.md"
          - "styles/align.md"
          - "styles/background.md"
          - "styles/background_tint.md"
          - "styles/border.md"
          - "styles/border_subtitle_align.md"
          - "styles/border_subtitle_background.md"
          - "styles/border_subtitle_color.md"
          - "styles/border_subtitle_style.md"
          - "styles/border_title_align.md"
          - "styles/border_title_background.md"
          - "styles/border_title_color.md"
          - "styles/border_title_style.md"
          - "styles/box_sizing.md"
          - "styles/color.md"
          - "styles/content_align.md"
          - "styles/display.md"
          - "styles/dock.md"
          - Grid:
              - "styles/grid/index.md"
              - "styles/grid/column_span.md"
              - "styles/grid/grid_columns.md"
              - "styles/grid/grid_gutter.md"
              - "styles/grid/grid_rows.md"
              - "styles/grid/grid_size.md"
              - "styles/grid/row_span.md"
          - "styles/hatch.md"
          - "styles/height.md"
          - "styles/keyline.md"
          - "styles/layer.md"
          - "styles/layers.md"
          - "styles/layout.md"
          - Links:
              - "styles/links/index.md"
              - "styles/links/link_background.md"
              - "styles/links/link_background_hover.md"
              - "styles/links/link_color.md"
              - "styles/links/link_color_hover.md"
              - "styles/links/link_style.md"
              - "styles/links/link_style_hover.md"
          - "styles/margin.md"
          - "styles/max_height.md"
          - "styles/max_width.md"
          - "styles/min_height.md"
          - "styles/min_width.md"
          - "styles/offset.md"
          - "styles/opacity.md"
          - "styles/outline.md"
          - "styles/overflow.md"
          - "styles/padding.md"
          - "styles/position.md"
          - Scrollbar colors:
              - "styles/scrollbar_colors/index.md"
              - "styles/scrollbar_colors/scrollbar_background.md"
              - "styles/scrollbar_colors/scrollbar_background_active.md"
              - "styles/scrollbar_colors/scrollbar_background_hover.md"
              - "styles/scrollbar_colors/scrollbar_color.md"
              - "styles/scrollbar_colors/scrollbar_color_active.md"
              - "styles/scrollbar_colors/scrollbar_color_hover.md"
              - "styles/scrollbar_colors/scrollbar_corner_color.md"
          - "styles/scrollbar_gutter.md"
          - "styles/scrollbar_size.md"
          - "styles/scrollbar_visibility.md"
          - "styles/text_align.md"
          - "styles/text_opacity.md"
          - "styles/text_overflow.md"
          - "styles/text_wrap.md"
          - "styles/text_style.md"
          - "styles/tint.md"
          - "styles/visibility.md"
          - "styles/width.md"
      - Widgets:
          - "widgets/button.md"
          - "widgets/checkbox.md"
          - "widgets/collapsible.md"
          - "widgets/content_switcher.md"
          - "widgets/data_table.md"
          - "widgets/digits.md"
          - "widgets/directory_tree.md"
          - "widgets/footer.md"
          - "widgets/header.md"
          - "widgets/index.md"
          - "widgets/input.md"
          - "widgets/label.md"
          - "widgets/link.md"
          - "widgets/list_item.md"
          - "widgets/list_view.md"
          - "widgets/loading_indicator.md"
          - "widgets/log.md"
          - "widgets/markdown_viewer.md"
          - "widgets/markdown.md"
          - "widgets/masked_input.md"
          - "widgets/option_list.md"
          - "widgets/placeholder.md"
          - "widgets/pretty.md"
          - "widgets/progress_bar.md"
          - "widgets/radiobutton.md"
          - "widgets/radioset.md"
          - "widgets/rich_log.md"
          - "widgets/rule.md"
          - "widgets/select.md"
          - "widgets/selection_list.md"
          - "widgets/sparkline.md"
          - "widgets/static.md"
          - "widgets/switch.md"
          - "widgets/tabbed_content.md"
          - "widgets/tabs.md"
          - "widgets/text_area.md"
          - "widgets/toast.md"
          - "widgets/tree.md"
  - API:
      - "api/index.md"
      - "api/app.md"
      - "api/await_complete.md"
      - "api/await_remove.md"
      - "api/binding.md"
      - "api/cache.md"
      - "api/color.md"
      - "api/command.md"
      - "api/constants.md"
      - "api/containers.md"
      - "api/compose.md"
      - "api/content.md"
      - "api/coordinate.md"
      - "api/dom_node.md"
      - "api/events.md"
      - "api/errors.md"
      - "api/filter.md"
      - "api/fuzzy_matcher.md"
      - "api/geometry.md"
      - "api/getters.md"
      - "api/highlight.md"
      - "api/layout.md"
      - "api/lazy.md"
      - "api/logger.md"
      - "api/logging.md"
      - "api/map_geometry.md"
      - "api/markup.md"
      - "api/message_pump.md"
      - "api/message.md"
      - "api/on.md"
      - "api/pilot.md"
      - "api/query.md"
      - "api/reactive.md"
      - "api/renderables.md"
      - "api/screen.md"
      - "api/scrollbar.md"
      - "api/scroll_view.md"
      - "api/signal.md"
      - "api/strip.md"
      - "api/suggester.md"
      - "api/system_commands_source.md"
      - "api/timer.md"
      - "api/types.md"
      - "api/validation.md"
      - "api/walk.md"
      - "api/widget.md"
      - "api/work.md"
      - "api/worker.md"
      - "api/worker_manager.md"
  - "How To":
      - "how-to/index.md"
      - "how-to/center-things.md"
      - "how-to/design-a-layout.md"
      - "how-to/package-with-hatch.md"
      - "how-to/render-and-compose.md"
      - "how-to/style-inline-apps.md"
      - "how-to/work-with-containers.md"
  - "FAQ.md"
  - "roadmap.md"
  - "Blog":
      - blog/index.md



================================================
FILE: mkdocs-offline.yml
================================================
INHERIT: mkdocs-common.yml

plugins:
  offline:
  exclude:
    glob:
      - "**/_template.md"
      - blog/*

site_dir: docs-offline



================================================
FILE: mkdocs-online.yml
================================================
INHERIT: mkdocs-common.yml

repo_url: https://github.com/textualize/textual/
site_url: https://textual.textualize.io/
edit_uri: edit/main/docs/

plugins:
  blog:
  rss:
    match_path: blog/posts/.*
    date_from_meta:
      as_creation: date
    categories:
      - categories
      - release
      - tags
  mkdocstrings:
    handlers:
      python:
        import:
          - https://docs.python.org/3/objects.inv
          - https://rich.readthedocs.io/en/stable/objects.inv



================================================
FILE: mypy.ini
================================================
[mypy]

[mypy-pygments.*]
ignore_missing_imports = True

[mypy-IPython.*]
ignore_missing_imports = True

[mypy-commonmark.*]
ignore_missing_imports = True

[mypy-colorama.*]
ignore_missing_imports = True

[mypy-ipywidgets.*]
ignore_missing_imports = True



================================================
FILE: pyproject.toml
================================================
[tool.poetry]
name = "textual"
version = "6.4.0"
homepage = "https://github.com/Textualize/textual"
repository = "https://github.com/Textualize/textual"
documentation = "https://textual.textualize.io/"

description = "Modern Text User Interface framework"
authors = ["Will McGugan <will@textualize.io>"]
license = "MIT"
readme = "README.md"
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "Operating System :: Microsoft :: Windows :: Windows 11",
    "Operating System :: MacOS",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Typing :: Typed",
]
include = [
    "src/textual/py.typed",
    { path = "docs/examples", format = "sdist" },
    { path = "tests", format = "sdist" },
    # The reason for the slightly convoluted path specification here is that
    # poetry populates the exclude list with the content of .gitignore, and
    # it also seems like exclude trumps include. So here we specify that we
    # want to package up the content of the docs-offline directory in a way
    # that works around that.
    { path = "docs-offline/**/*", format = "sdist" },
]

[tool.poetry.urls]
"Bug Tracker" = "https://github.com/Textualize/textual/issues"

[tool.ruff]
target-version = "py39"

[tool.poetry.dependencies]
python = "^3.9"
markdown-it-py = { extras = ["linkify"], version = ">=2.1.0" }
mdit-py-plugins = "*"
rich = ">=14.2.0"
#rich = {path="../rich", develop=true}
typing-extensions = "^4.4.0"
platformdirs = ">=3.6.0,<5"

# start of [syntax] extras
# Require tree-sitter >= 0.25.0 and python >= 3.10
# Windows, MacOS and Linux binary wheels are available for all of the languages below.
tree-sitter = { version = ">=0.25.0", optional = true, python = ">=3.10" }
tree-sitter-python = { version = ">=0.23.0", optional = true, python = ">=3.10" }
tree-sitter-markdown = { version = ">=0.3.0", optional = true, python = ">=3.10"}
tree-sitter-json = { version = ">=0.24.0", optional = true, python = ">=3.10" }
tree-sitter-toml = { version = ">=0.6.0", optional = true, python = ">=3.10" }
tree-sitter-yaml = { version = ">=0.6.0", optional = true, python = ">=3.10" }
tree-sitter-html = { version = ">=0.23.0", optional = true, python = ">=3.10" }
tree-sitter-css = { version = ">=0.23.0", optional = true, python = ">=3.10" }
tree-sitter-javascript = { version = ">=0.23.0", optional = true, python = ">=3.10" }
tree-sitter-rust = { version = ">=0.23.0", optional = true, python = ">=3.10" }
tree-sitter-go = { version = ">=0.23.0", optional = true, python = ">=3.10" }
tree-sitter-regex = { version = ">=0.24.0", optional = true, python = ">=3.10" }
tree-sitter-xml = { version = ">=0.7.0", optional = true, python = ">=3.10" }
tree-sitter-sql = { version = ">=0.3.11", optional = true, python = ">=3.10" }
tree-sitter-java = { version = ">=0.23.0", optional = true, python = ">=3.10" }
tree-sitter-bash = { version = ">=0.23.0", optional = true, python = ">=3.10" }
# end of [syntax] extras
pygments = "^2.19.2"

[tool.poetry.extras]
syntax = [
    "tree-sitter",
    "tree-sitter-python",
    "tree-sitter-markdown",
    "tree-sitter-json",
    "tree-sitter-toml",
    "tree-sitter-yaml",
    "tree-sitter-html",
    "tree-sitter-css",
    "tree-sitter-javascript",
    "tree-sitter-rust",
    "tree-sitter-go",
    "tree-sitter-regex",
    "tree-sitter-xml",
    "tree-sitter-sql",
    "tree-sitter-java",
    "tree-sitter-bash",
]

[tool.poetry.group.dev.dependencies]
black = "24.4.2"
griffe = "0.32.3"
httpx = "^0.23.1"
mkdocs = "^1.3.0"
mkdocs-exclude = "^1.0.2"
mkdocs-git-revision-date-localized-plugin = "^1.2.5"
mkdocs-material = "^9.0.11"
mkdocs-rss-plugin = "^1.5.0"
mkdocstrings = { extras = ["python"], version = "^0.20.0" }
mkdocstrings-python = "^1.0.0"
mypy = "^1.0.0"
pre-commit = "^2.13.0"
pytest = "^8.3.1"
pytest-xdist = "^3.6.1"
pytest-asyncio = "*"
pytest-cov = "^5.0.0"
textual-dev = "^1.7.0"
types-setuptools = "^67.2.0.1"
isort = "^5.13.2"
pytest-textual-snapshot = "^1.0.0"

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
addopts = "--strict-markers"
markers = [
    "syntax: marks tests that require syntax highlighting (deselect with '-m \"not syntax\"')",
]
asyncio_default_fixture_loop_scope = "function"

[build-system]
requires = ["poetry-core>=1.2.0"]
build-backend = "poetry.core.masonry.api"



================================================
FILE: .coveragerc
================================================
[run]
omit =

[report]
exclude_lines =
    pragma: no cover
    if TYPE_CHECKING:
    if __name__ == "__main__":
    @overload
    __rich_repr__
    @abstractmethod



================================================
FILE: .deepsource.toml
================================================
version = 1

[[analyzers]]
name = "python"

  [analyzers.meta]
  runtime_version = "3.x.x"



================================================
FILE: .pre-commit-config.yaml
================================================
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0
    hooks:
      - id: check-ast  # simply checks whether the files parse as valid python
      - id: check-builtin-literals  # requires literal syntax when initializing empty or zero python builtin types
      - id: check-case-conflict  # checks for files that would conflict in case-insensitive filesystems
      - id: check-merge-conflict  # checks for files that contain merge conflict strings
      - id: check-json  # checks json files for parseable syntax
      - id: check-toml  # checks toml files for parseable syntax
      - id: check-yaml  # checks yaml files for parseable syntax
        args: [ '--unsafe' ]  # Instead of loading the files, simply parse them for syntax.
      - id: check-shebang-scripts-are-executable  # ensures that (non-binary) files with a shebang are executable
      - id: check-vcs-permalinks  # ensures that links to vcs websites are permalinks
      - id: end-of-file-fixer  # ensures that a file is either empty, or ends with one newline
      - id: mixed-line-ending  # replaces or checks mixed line ending
  - repo: https://github.com/pycqa/isort
    rev: '5.13.2'
    hooks:
      - id: isort
        name: isort (python)
        language_version: '3.11'
        args: ['--profile', 'black', '--filter-files']
  - repo: https://github.com/psf/black
    rev: '24.1.1'
    hooks:
      - id: black
  - repo: https://github.com/hadialqattan/pycln  # removes unused imports
    rev: v2.5.0
    hooks:
      - id: pycln
        language_version: '3.11'
        args: [--all]
  - repo: https://github.com/MarcoGorelli/absolufy-imports
    rev: v0.3.1
    hooks:
      - id: absolufy-imports
exclude: ^tests/snapshot_tests



================================================
FILE: docs/CNAME
================================================
textual.textualize.io



================================================
FILE: docs/FAQ.md
================================================
---
hide:
  - navigation
---

<!-- Auto-generated by FAQtory -->
<!-- Do not edit by hand! -->

# Frequently Asked Questions


Welcome to the Textual FAQ.
Here we try and answer any question that comes up frequently.
If you can't find what you are looking for here, see our other [help](./help.md) channels.

<a name="does-textual-support-images"></a>
## Does Textual support images?

Textual doesn't have built-in support for images yet, but it is on the [Roadmap](https://textual.textualize.io/roadmap/).

See also the [rich-pixels](https://github.com/darrenburns/rich-pixels) project for a Rich renderable for images that works with Textual.

---

<a name="how-can-i-fix-importerror-cannot-import-name-composeresult-from-textualapp-"></a>
## How can I fix ImportError cannot import name ComposeResult from textual.app ?

You likely have an older version of Textual. You can install the latest version by adding the `-U` switch which will force pip to upgrade.

The following should do it:

```
pip install textual-dev -U
```

---

<a name="how-can-i-select-and-copy-text-in-a-textual-app"></a>
## How can I select and copy text in a Textual app?

Textual supports text selection for most widgets, via click and drag. Press ctrl+c to copy.

For widgets that don't yet support text selection, you can try and use your terminal's builtin support.
Most terminal emulators offer a modifier key which you can hold while you click and drag to restore the behavior you
may expect from the command line. The exact modifier key depends on the terminal and platform you are running on.

- **iTerm** Hold the OPTION key.
- **Gnome Terminal** Hold the SHIFT key.
- **Windows Terminal** Hold the SHIFT key.

Refer to the documentation for your terminal emulator, if it is not listed above.

---

<a name="how-can-i-set-a-translucent-app-background"></a>
## How can I set a translucent app background?

Some terminal emulators have a translucent background feature which allows the desktop underneath to be partially visible.

This feature is unlikely to work with Textual, as the translucency effect requires the use of ANSI background colors, which Textual doesn't use.
Textual uses 16.7 million colors where available which enables consistent colors across all platforms and additional effects which aren't possible with ANSI colors.

For more information on ANSI colors in Textual, see [Why no ANSI Themes?](#why-doesnt-textual-support-ansi-themes).

---

<a name="how-do-i-center-a-widget-in-a-screen"></a>
## How do I center a widget in a screen?

!!! tip

    See [*How To Center Things*](https://textual.textualize.io/how-to/center-things/) in the
    Textual documentation for a more comprehensive answer to this question.

To center a widget within a container use
[`align`](https://textual.textualize.io/styles/align/). But remember that
`align` works on the *children* of a container, it isn't something you use
on the child you want centered.

For example, here's an app that shows a `Button` in the middle of a
`Screen`:

```python
from textual.app import App, ComposeResult
from textual.widgets import Button

class ButtonApp(App):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Button("PUSH ME!")

if __name__ == "__main__":
    ButtonApp().run()
```

If you use the above on multiple widgets, you'll find they appear to
"left-align" in the center of the screen, like this:

```
+-----+
|     |
+-----+

+---------+
|         |
+---------+

+---------------+
|               |
+---------------+
```

If you want them more like this:

```
     +-----+
     |     |
     +-----+

   +---------+
   |         |
   +---------+

+---------------+
|               |
+---------------+
```

The best approach is to wrap each widget in a [`Center`
container](https://textual.textualize.io/api/containers/#textual.containers.Center)
that individually centers it. For example:

```python
from textual.app import App, ComposeResult
from textual.containers import Center
from textual.widgets import Button

class ButtonApp(App):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Center(Button("PUSH ME!"))
        yield Center(Button("AND ME!"))
        yield Center(Button("ALSO PLEASE PUSH ME!"))
        yield Center(Button("HEY ME ALSO!!"))

if __name__ == "__main__":
    ButtonApp().run()
```

---

<a name="how-do-i-fix-workerdeclarationerror"></a>
## How do I fix WorkerDeclarationError?

Textual version 0.31.0 requires that you set `thread=True` on the `@work` decorator if you want to run a threaded worker.

If you want a threaded worker, you would declare it in the following way:

```python
@work(thread=True)
def run_in_background():
    ...
```

If you *don't* want a threaded worker, you should make your work function `async`:

```python
@work()
async def run_in_background():
    ...
```

This change was made because it was too easy to accidentally create a threaded worker, which may produce unexpected results.

---

<a name="how-do-i-pass-arguments-to-an-app"></a>
## How do I pass arguments to an app?

When creating your `App` class, override `__init__` as you would when
inheriting normally. For example:

```python
from textual.app import App, ComposeResult
from textual.widgets import Static

class Greetings(App[None]):

    def __init__(self, greeting: str="Hello", to_greet: str="World") -> None:
        self.greeting = greeting
        self.to_greet = to_greet
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Static(f"{self.greeting}, {self.to_greet}")
```

Then the app can be run, passing in various arguments; for example:

```python
# Running with default arguments.
Greetings().run()

# Running with a keyword argument.
Greetings(to_greet="davep").run()

# Running with both positional arguments.
Greetings("Well hello", "there").run()
```

---

<a name="why-do-some-key-combinations-never-make-it-to-my-app"></a>
## Why do some key combinations never make it to my app?

Textual can only ever support key combinations that are passed on by your
terminal application. Which keys get passed on can differ from terminal to
terminal, and from operating system to operating system.

Because of this it's best to stick to key combinations that are known to be
universally-supported; these include the likes of:

- Letters
- Numbers
- Numbered function keys (especially F1 through F10)
- Space
- Return
- Arrow, home, end and page keys
- Control
- Shift

When [creating bindings for your
application](https://textual.textualize.io/guide/input/#bindings) we
recommend picking keys and key combinations from the above.

Keys that aren't normally passed through by terminals include Cmd and Option
on macOS, and the Windows key on Windows.

If you need to test what [key
combinations](https://textual.textualize.io/guide/input/#keyboard-input)
work in different environments you can try them out with `textual keys`.

---

<a name="why-doesnt-textual-look-good-on-macos"></a>
## Why doesn't Textual look good on macOS?

You may find that the default macOS Terminal.app doesn't render Textual apps (and likely other TUIs) very well, particularly when it comes to box characters.
For instance, you may find it displays misaligned blocks and lines like this:

<img width="1042" alt="Screenshot 2023-06-19 at 10 43 02" src="https://github.com/Textualize/textual/assets/554369/e61f3876-3dd1-4ac8-b380-22922c89c7d6">

You can (mostly) fix this by opening settings -> profiles > Text tab, and changing the font settings.
We have found that Menlo Regular font, with a character spacing of 1 and line spacing of 0.805 produces reasonable results.
If you want to use another font, you may have to tweak the line spacing until you get good results.

<img width="737" alt="Screenshot 2023-06-19 at 10 44 00" src="https://github.com/Textualize/textual/assets/554369/0a052a93-b1fd-4327-9d33-d954b51a9ad2">

With these changes, Textual apps render more as intended:

<img width="1042" alt="Screenshot 2023-06-19 at 10 43 23" src="https://github.com/Textualize/textual/assets/554369/a0c4aa05-c509-4ac1-b0b8-e68ce4433f70">

Even with this *fix*, Terminal.app has a few limitations.
It is limited to 256 colors, and can be a little slow compared to more modern alternatives.
Fortunately there are a number of free terminal emulators for macOS which produces high quality results.

We recommend any of the following terminals:

- [iTerm2](https://iterm2.com/)
- [Kitty](https://sw.kovidgoyal.net/kitty/)
- [WezTerm](https://wezfurlong.org/wezterm/)

### Terminal.app colors

<img width="762" alt="Screenshot 2023-06-19 at 11 00 12" src="https://github.com/Textualize/textual/assets/554369/e0555d23-e141-4069-b318-f3965c880208">

### iTerm2 colors

<img width="1002" alt="Screenshot 2023-06-19 at 11 00 25" src="https://github.com/Textualize/textual/assets/554369/9a8cde57-5121-49a7-a2e0-5f6fc871b7a6">

---

<a name="why-doesnt-textual-support-ansi-themes"></a>
## Why doesn't Textual support ANSI themes?

Textual will not generate escape sequences for the 16 themeable *ANSI* colors.

This is an intentional design decision we took for for the following reasons:

- Not everyone has a carefully chosen ANSI color theme. Color combinations which may look fine on your system, may be unreadable on another machine. There is very little an app author or Textual can do to resolve this. Asking users to simply pick a better theme is not a good solution, since not all users will know how.
- ANSI colors can't be manipulated in the way Textual can do with other colors. Textual can blend colors and produce light and dark shades from an original color, which is used to create more readable text and user interfaces. Color blending will also be used to power future accessibility features.

Textual has a design system which guarantees apps will be readable on all platforms and terminals, and produces better results than ANSI colors.

There is currently a light and dark version of the design system, but more are planned. It will also be possible for users to customize the source colors on a per-app or per-system basis. This means that in the future you will be able to modify the core colors to blend in with your chosen terminal theme.

!!! tip "Changed in version 0.80.0"

    Textual added an `ansi_color` boolean to App. If you set this to `True`, then Textual will not attempt to convert ANSI colors. Note that you will lose transparency effects if you enable this setting.

---

Generated by [FAQtory](https://github.com/willmcgugan/faqtory)



================================================
FILE: docs/getting_started.md
================================================

All you need to get started building Textual apps.

## Requirements

Textual requires Python 3.9 or later (if you have a choice, pick the most recent Python). Textual runs on Linux, macOS, Windows and probably any OS where Python also runs.

!!! info "Your platform"

    ### :fontawesome-brands-linux: Linux (all distros)

    All Linux distros come with a terminal emulator that can run Textual apps.

    ### :material-apple: macOS

    The default terminal app is limited to 256 colors. We recommend installing a newer terminal such as [iterm2](https://iterm2.com/), [Ghostty](https://ghostty.org/), [Kitty](https://sw.kovidgoyal.net/kitty/), or [WezTerm](https://wezfurlong.org/wezterm/).

    ### :material-microsoft-windows: Windows

    The new [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-gb&gl=GB) runs Textual apps beautifully.


## Installation

Here's how to install Textual.

### From PyPI

You can install Textual via PyPI, with the following command:

```
pip install textual
```

If you plan on developing Textual apps, you should also install textual developer tools:

```
pip install textual-dev
```

If you would like to enable syntax highlighting in the [TextArea](./widgets/text_area.md) widget, you should specify the "syntax" extras when you install Textual:

```
pip install "textual[syntax]"
```

### From conda-forge

Textual is also available on [conda-forge](https://conda-forge.org/). The preferred package manager for conda-forge is currently [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html):

```
micromamba install -c conda-forge textual
```

And for the textual developer tools:

```
micromamba install -c conda-forge textual-dev
```

### Textual CLI

If you installed the developer tools you should have access to the `textual` command. There are a number of sub-commands available which will aid you in building Textual apps. Run the following for a list of the available commands:

```bash
textual --help
```

See [devtools](guide/devtools.md) for more about the `textual` command.

## Demo

Once you have Textual installed, run the following to get an impression of what it can do:

```bash
python -m textual
```

## Examples


The Textual repository comes with a number of example apps. To try out the examples, first clone the Textual repository:

=== "HTTPS"

    ```bash
    git clone https://github.com/Textualize/textual.git
    ```

=== "SSH"

    ```bash
    git clone git@github.com:Textualize/textual.git
    ```

=== "GitHub CLI"

    ```bash
    gh repo clone Textualize/textual
    ```


With the repository cloned, navigate to the `/examples/` directory where you will find a number of Python files you can run from the command line:

```bash
cd textual/examples/
python code_browser.py ../
```

### Widget examples

In addition to the example apps, you can also find the code listings used to generate the screenshots in these docs in the `docs/examples` directory.

## Need help?

See the [help](./help.md) page for how to get help with Textual, or to report bugs.



================================================
FILE: docs/help.md
================================================
# Help

If you need help with any aspect of Textual, let us know! We would be happy to hear from you.

## Bugs and feature requests

Report bugs via GitHub on the Textual [issues](https://github.com/Textualize/textual/issues) page. You can also post feature requests via GitHub issues, but see the [Roadmap](./roadmap.md) first.

## Help with using Textual

You can seek help with using Textual [in the discussion area on GitHub](https://github.com/Textualize/textual/discussions).

## Discord Server

For more realtime feedback or chat, join our Discord server to connect with the [Textual community](https://discord.gg/Enf6Z3qhVr).



================================================
FILE: docs/index.md
================================================
---
hide:
  - toc
  - navigation
---

!!! tip inline end

    See the navigation links in the header or side-bar.

    Click :octicons-three-bars-16: (top left) on mobile.


# Welcome

Welcome to the [Textual](https://github.com/Textualize/textual) framework documentation.

[Get started](./getting_started.md){ .md-button .md-button--primary } or go straight to the [Tutorial](./tutorial.md)



## What is Textual?

Textual is a *Rapid Application Development* framework for Python, built by [Textualize.io](https://www.textualize.io).


Build sophisticated user interfaces with a simple Python API. Run your apps in the terminal *or* a [web browser](https://github.com/Textualize/textual-serve)!



<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } :material-language-python:{. lg .middle } __Rapid development__

    ---

    Uses your existing Python skills to build beautiful user interfaces.


-   :material-raspberry-pi:{ .lg .middle } __Low requirements__

    ---

    Run Textual on a single board computer if you want to.



-   :material-microsoft-windows:{ .lg .middle } :material-apple:{ .lg .middle } :fontawesome-brands-linux:{ .lg .middle } __Cross platform__

    ---

    Textual runs just about everywhere.



-   :material-network:{ .lg .middle } __Remote__

    ---

    Textual apps can run over SSH.


-   :fontawesome-solid-terminal:{ .lg .middle } __CLI Integration__

    ---

    Textual apps can be launched and run from the command prompt.



-   :material-scale-balance:{ .lg .middle } __Open Source__

    ---

    Textual is licensed under MIT.


</div>



---

# Built with Textual

Textual has enabled an ecosystem of applications and tools for developers and non-developers alike.

Here are a few examples.


## Posting

The API client that lives in your terminal.
Posting is a beautiful open-source terminal app for developing and testing APIs.

[Posting Website](https://posting.sh/)

[Posting Github Repository](https://github.com/darrenburns/posting)

<div>
<a href="https://posting.sh">
--8<-- "docs/images/screenshots/posting.svg"
</a>
</div>

---

## Toolong

A terminal application to view, tail, merge, and search log files (plus JSONL).

[Toolong Github Repository](https://github.com/textualize/toolong)

<div>
<a href="https://github.com/Textualize/toolong">
--8<-- "docs/images/screenshots/toolong.svg"
</a>
</div>

---


## Memray

Memray is a memory profiler for Python, built by Bloomberg.

[Memray Github Repository](https://github.com/bloomberg/memray)

<div>
<a href="https://github.com/bloomberg/memray">
--8<-- "docs/images/screenshots/memray.svg"
</a>
</div>

---

## Dolphie

Your single pane of glass for real-time analytics into MySQL/MariaDB & ProxySQL

[Dolphie Github Repository](https://github.com/charles-001/dolphie)


<div>
<a href="https://github.com/charles-001/dolphie">
--8<-- "docs/images/screenshots/dolphie.svg"
</a>
</div>


---

## Harlequin

An easy, fast, and beautiful database client for the terminal.

[Harlequin website](https://harlequin.sh/)

<div>
<a href="https://harlequin.sh">
--8<-- "docs/images/screenshots/harlequin.svg"
</a>
</div>



---

# Examples

The following examples are taken from the [examples directory](https://github.com/Textualize/textual/tree/main/examples).

Click the tabs to see the code behind the example.

=== "Pride example"

    ```{.textual path="examples/pride.py"}
    ```

=== "pride.py"

    ```py
    --8<-- "examples/pride.py"
    ```


---

=== "Calculator example"

    ```{.textual path="examples/calculator.py" columns=100 lines=41 press="6,.,2,8,3,1,8,5,3,0,7,1,wait:400"}
    ```

=== "calculator.py"

    ```python
    --8<-- "examples/calculator.py"
    ```

=== "calculator.tcss"

    ```css
    --8<-- "examples/calculator.tcss"
    ```



================================================
FILE: docs/roadmap.md
================================================
---
hide:
  - navigation
---


# Roadmap

We ([textualize.io](https://www.textualize.io/)) are actively building and maintaining Textual.

We have many new features in the pipeline. This page will keep track of that work.

## Features

High-level features we plan on implementing.

- [ ] Accessibility
    * [ ] Integration with screen readers
    * [x] Monochrome mode
    * [ ] High contrast theme
    * [ ] Color-blind themes
- [X] Command palette
    * [X] Fuzzy search
- [ ] Configuration (.toml based extensible configuration format)
- [x] Console
- [ ] Devtools
    * [ ] Integrated log
    * [ ] DOM tree view
    * [ ] REPL
- [ ] Reactive state abstraction
- [x] Themes
    * [ ] Customize via config
    * [ ] Builtin theme editor

## Widgets

Widgets are key to making user-friendly interfaces. The builtin widgets should cover many common (and some uncommon) use-cases. The following is a list of the widgets we have built or are planning to build.

- [x] Buttons
    * [x] Error / warning variants
- [ ] Color picker
- [X] Checkbox
- [X] Content switcher
- [x] DataTable
    * [x] Cell select
    * [x] Row / Column select
    * [x] API to update cells / rows
    * [ ] Lazy loading API
- [ ] Date picker
- [ ] Drop-down menus
- [ ] Form Widget
    * [ ] Serialization / Deserialization
    * [ ] Export to `attrs` objects
    * [ ] Export to `PyDantic` objects
- [ ] Image support
    * [ ] Half block
    * [ ] Braille
    * [ ] Sixels, and other image extensions
- [x] Input
    * [x] Validation
    * [ ] Error / warning states
    * [ ] Template types: IP address, physical units (weight, volume), currency, credit card etc
- [X] Select control (pull-down)
- [X] Markdown viewer
    * [ ] Collapsible sections
    * [ ] Custom widgets
- [ ] Plots
    * [ ] bar chart
    * [ ] line chart
    * [ ] Candlestick chars
- [X] Progress bars
    * [ ] Style variants (solid, thin etc)
- [X] Radio boxes
- [X] Spark-lines
- [X] Switch
- [X] Tabs
- [X] TextArea (multi-line input)
    * [X] Basic controls
    * [ ] Indentation guides
    * [ ] Smart features for various languages
    * [X] Syntax highlighting



================================================
FILE: docs/robots.txt
================================================
Sitemap: https://textual.textualize.io/sitemap.xml



================================================
FILE: docs/tutorial.md
================================================
---
hide:
  - navigation
---

# Tutorial

Welcome to the Textual Tutorial!

By the end of this page you should have a solid understanding of app development with Textual.

!!! quote

    If you want people to build things, make it fun.

    &mdash; **Will McGugan** (creator of Rich and Textual)

## Video series

This tutorial has an accompanying [video series](https://www.youtube.com/playlist?list=PLHhDR_Q5Me1MxO4LmfzMNNQyKfwa275Qe) which covers the same content.

## Stopwatch Application

We're going to build a stopwatch application. This application should show a list of stopwatches with buttons to start, stop, and reset the stopwatches. We also want the user to be able to add and remove stopwatches as required.

This will be a simple yet **fully featured** app &mdash; you could distribute this app if you wanted to!

Here's what the finished app will look like:


```{.textual path="docs/examples/tutorial/stopwatch.py" title="stopwatch.py" press="tab,enter,tab,enter,tab,enter,tab,enter"}
```

!!! info

    Did you notice the `^p palette` at the bottom right hand corner?
    This is the [Command Palette](./guide/command_palette.md).
    You can think of it as a dedicated command prompt for your app.

### Get the code

If you want to try the finished Stopwatch app and follow along with the code, first make sure you have [Textual installed](getting_started.md) then check out the [Textual](https://github.com/Textualize/textual) repository:

=== "HTTPS"

    ```bash
    git clone https://github.com/Textualize/textual.git
    ```

=== "SSH"

    ```bash
    git clone git@github.com:Textualize/textual.git
    ```

=== "GitHub CLI"

    ```bash
    gh repo clone Textualize/textual
    ```


With the repository cloned, navigate to `docs/examples/tutorial` and run `stopwatch.py`.

```bash
cd textual/docs/examples/tutorial
python stopwatch.py
```

## Type hints (in brief)

!!! tip inline end

    Type hints are entirely optional in Textual. We've included them in the example code but it's up to you whether you add them to your own projects.

We're a big fan of Python type hints at Textualize. If you haven't encountered type hinting, it's a way to express the types of your data, parameters, and return values. Type hinting allows tools like [mypy](https://mypy.readthedocs.io/en/stable/) to catch bugs before your code runs.

The following function contains type hints:

```python
def repeat(text: str, count: int) -> str:
    """Repeat a string a given number of times."""
    return text * count
```

Parameter types follow a colon. So `text: str` indicates that `text` requires a string and `count: int` means that `count` requires an integer.

Return types follow `->`. So `-> str:` indicates this method returns a string.


## The App class

The first step in building a Textual app is to import and extend the `App` class. Here's a basic app class we will use as a starting point for the stopwatch app.

```python title="stopwatch01.py"
--8<-- "docs/examples/tutorial/stopwatch01.py"
```

If you run this code, you should see something like the following:


```{.textual path="docs/examples/tutorial/stopwatch01.py" title="stopwatch01.py"}
```

Hit the ++d++ key to toggle between light and dark themes.

```{.textual path="docs/examples/tutorial/stopwatch01.py" press="d" title="stopwatch01.py"}
```

Hit ++ctrl+q++ to exit the app and return to the command prompt.

### A closer look at the App class

Let's examine `stopwatch01.py` in more detail.

```python title="stopwatch01.py" hl_lines="1 2"
--8<-- "docs/examples/tutorial/stopwatch01.py"
```

The first line imports `App` class, which is the base class for all Textual apps.
The second line imports two builtin widgets: [`Footer`](widgets/footer.md) which shows a bar at the bottom of the screen with bound keys, and [`Header`](widgets/header.md) which shows a title at the top of the screen.
Widgets are re-usable components responsible for managing a part of the screen.
We will cover how to build widgets in this tutorial.

The following lines define the app itself:

```python title="stopwatch01.py" hl_lines="5-19"
--8<-- "docs/examples/tutorial/stopwatch01.py"
```

The App class is where most of the logic of Textual apps is written. It is responsible for loading configuration, setting up widgets, handling keys, and more.

Here's what the above app defines:

- `BINDINGS` is a list of tuples that maps (or *binds*) keys to actions in your app. The first value in the tuple is the key; the second value is the name of the action; the final value is a short description. We have a single binding which maps the ++d++ key on to the "toggle_dark" action. See [key bindings](./guide/input.md#bindings) in the guide for details.

-  `compose()` is where we construct a user interface with widgets. The `compose()` method may return a list of widgets, but it is generally easier to _yield_ them (making this method a generator). In the example code we yield an instance of each of the widget classes we imported, i.e. `Header()` and `Footer()`.

- `action_toggle_dark()` defines an _action_ method. Actions are methods beginning with `action_` followed by the name of the action. The `BINDINGS` list above tells Textual to run this action when the user hits the ++d++ key. See [actions](./guide/actions.md) in the guide for details.

```python title="stopwatch01.py" hl_lines="22-24"
--8<-- "docs/examples/tutorial/stopwatch01.py"
```

The final three lines create an instance of the app and calls the [run()][textual.app.App.run] method which puts your terminal into *application mode* and runs the app until you exit with ++ctrl+q++. This happens within a `__name__ == "__main__"` block so we could run the app with `python stopwatch01.py` or import it as part of a larger project.

## Designing a UI with widgets

Textual has a large number of [builtin widgets](./widget_gallery.md).
For our app we will need new widgets, which we can create by extending and combining the builtin widgets.

Before we dive into building widgets, let's first sketch a design for the app &mdash; so we know what we're aiming for.


<div class="excalidraw">
--8<-- "docs/images/stopwatch.excalidraw.svg"
</div>

### Custom widgets

We need a `Stopwatch` widget composed of the following _child_ widgets:

- A "Start" button
- A "Stop" button
- A "Reset" button
- A time display

Let's add those to the app.
Just a skeleton for now, we will add the rest of the features as we go.

```python title="stopwatch02.py" hl_lines="2-3 6-7 10-18 30"
--8<-- "docs/examples/tutorial/stopwatch02.py"
```

We've imported two new widgets in this code: [`Button`](widgets/button.md) for the buttons and [`Digits`](widgets/digits.md) for the time display.
Additionally, we've imported [`HorizontalGroup`][textual.containers.HorizontalGroup] and [`VerticalScroll`][textual.containers.VerticalScroll] from `textual.containers` (as the name of the module suggests, *containers* are widgets which contain other widgets).
We will use these container widgets to define the general layout of our interface.

The `TimeDisplay` is currently very simple, all it does is extend `Digits` without adding any new features. We will flesh this out later.

The `Stopwatch` widget class extends the `HorizontalGroup` container class, which will arrange its children into a horizontal row. The Stopwatch's `compose()` adds those children, which correspond to the components from the sketch above.

!!! tip "Coordinating widgets"

    If you are building custom widgets of your own, be sure to see guide on [coordinating widgets](./guide/widgets.md#coordinating-widgets).

#### The buttons

The Button constructor takes a label to be displayed in the button (`"Start"`, `"Stop"`, or `"Reset"`). Additionally, some of the buttons set the following parameters:

- `id` is an identifier we can use to tell the buttons apart in code and apply styles. More on that later.
- `variant` is a string which selects a default style. The "success" variant makes the button green, and the "error" variant makes it red.

### Composing the widgets

The new line in `StopwatchApp.compose()` yields a single `VerticalScroll` which will scroll if the contents don't quite fit. This widget also takes care of key bindings required for scrolling, like ++up++, ++down++, ++page-down++, ++page-up++, ++home++, ++end++, etc.

When widgets contain other widgets (like `VerticalScroll`) they will typically accept their child widgets as positional arguments.
So the line `yield VerticalScroll(Stopwatch(), Stopwatch(), Stopwatch())` creates a `VerticalScroll` containing three `Stopwatch` widgets.


### The unstyled app

Let's see what happens when we run `stopwatch02.py`.

```{.textual path="docs/examples/tutorial/stopwatch02.py" title="stopwatch02.py"}
```

The elements of the stopwatch application are there, but it doesn't look much like the sketch. This is because we have yet to apply any _styles_ to our new widgets.

## Writing Textual CSS

Every widget has a `styles` object with a number of attributes that impact how the widget will appear. Here's how you might set white text and a blue background for a widget:

```python
self.styles.background = "blue"
self.styles.color = "white"
```

While it's possible to set all styles for an app this way, it is rarely necessary. Textual has support for CSS (Cascading Style Sheets), a technology used by web browsers. CSS files are data files loaded by your app which contain information about styles to apply to your widgets.

!!! info

    The dialect of CSS used in Textual is greatly simplified over web based CSS and easier to learn.


CSS makes it easy to iterate on the design of your app and enables [live-editing](./guide/devtools.md#live-editing) &mdash; you can edit CSS and see the changes without restarting the app!


Let's add a CSS file to our application.

```python title="stopwatch03.py" hl_lines="24"
--8<-- "docs/examples/tutorial/stopwatch03.py"
```

Adding the `CSS_PATH` class variable tells Textual to load the following file when the app starts:

```css title="stopwatch03.tcss"
--8<-- "docs/examples/tutorial/stopwatch03.tcss"
```

If we run the app now, it will look *very* different.

```{.textual path="docs/examples/tutorial/stopwatch03.py" title="stopwatch03.py"}
```

This app looks much more like our sketch. Let's look at how Textual uses `stopwatch03.tcss` to apply styles.

### CSS basics

CSS files contain a number of _declaration blocks_. Here's the first such block from `stopwatch03.tcss` again:

```css
Stopwatch {
    background: $boost;
    height: 5;
    margin: 1;
    min-width: 50;
    padding: 1;
}
```

The first line tells Textual that the styles should apply to the `Stopwatch` widget. The lines between the curly brackets contain the styles themselves.

Here's how this CSS code changes how the `Stopwatch` widget is displayed.

<div class="excalidraw">
--8<-- "docs/images/stopwatch_widgets.excalidraw.svg"
</div>

- `background: $boost` sets the background color to `$boost`. The `$` prefix picks a pre-defined color from the builtin theme. There are other ways to specify colors such as `"blue"` or `rgb(20,46,210)`.
- `height: 5` sets the height of our widget to 5 lines of text.
- `margin: 1` sets a margin of 1 cell around the `Stopwatch` widget to create a little space between widgets in the list.
- `min-width: 50` sets the minimum width of our widget to 50 cells.
- `padding: 1` sets a padding of 1 cell around the child widgets.


Here's the rest of `stopwatch03.tcss` which contains further declaration blocks:

```css
TimeDisplay {
    text-align: center;
    color: $foreground-muted;
    height: 3;
}

Button {
    width: 16;
}

#start {
    dock: left;
}

#stop {
    dock: left;
    display: none;
}

#reset {
    dock: right;
}
```

The `TimeDisplay` block aligns text to the center (`text-align:`), sets its color (`color:`), and sets its height (`height:`) to 3 lines.

The `Button` block sets the width (`width:`) of buttons to 16 cells (character widths).

The last 3 blocks have a slightly different format. When the declaration begins with a `#` then the styles will be applied to widgets with a matching "id" attribute. We've set an ID on the `Button` widgets we yielded in `compose`. For instance the first button has `id="start"` which matches `#start` in the CSS.

The buttons have a `dock` style which aligns the widget to a given edge.
The start and stop buttons are docked to the left edge, while the reset button is docked to the right edge.

You may have noticed that the stop button (`#stop` in the CSS) has `display: none;`. This tells Textual to not show the button. We do this because we don't want to display the stop button when the timer is *not* running. Similarly, we don't want to show the start button when the timer is running. We will cover how to manage such dynamic user interfaces in the next section.

### Dynamic CSS

We want our `Stopwatch` widget to have two states: a default state with a Start and Reset button; and a _started_ state with a Stop button. When a stopwatch is started it should also have a green background to indicate it is currently active.

<div class="excalidraw">
--8<-- "docs/images/css_stopwatch.excalidraw.svg"
</div>


We can accomplish this with a CSS _class_. Not to be confused with a Python class, a CSS class is like a tag you can add to a widget to modify its styles. A widget may have any number of CSS classes, which may be added and removed to change its appearance.

Here's the new CSS:

```css title="stopwatch04.tcss" hl_lines="32-52"
--8<-- "docs/examples/tutorial/stopwatch04.tcss"
```

These new rules are prefixed with `.started`. The `.` indicates that `.started` refers to a CSS class called "started". The new styles will be applied only to widgets that have this CSS class.

Some of the new styles have more than one selector separated by a space. The space indicates that the rule should match the second selector if it is a child of the first. Let's look at one of these styles:

```css
.started #start {
    display: none
}
```

The `.started` selector matches any widget with a `"started"` CSS class.
While `#start` matches a widget with an ID of `"start"`.
Combining the two selectors with a space (`.started #start`) creates a new selector that will match the start button *only* if it is also inside a container with a CSS class of "started".

As before, the `display: none` rule will cause any matching widgets to be hidden from view.

If we were to write this in English, it would be something like: "Hide the start button if the widget is already started".

### Manipulating classes

Modifying a widget's CSS classes is a convenient way to update visuals without introducing a lot of messy display related code.

You can add and remove CSS classes with the [add_class()][textual.dom.DOMNode.add_class] and [remove_class()][textual.dom.DOMNode.remove_class] methods.
We will use these methods to connect the started state to the Start / Stop buttons.

The following code will start or stop the stopwatches in response to clicking a button:

```python title="stopwatch04.py" hl_lines="13-18"
--8<-- "docs/examples/tutorial/stopwatch04.py"
```

The `on_button_pressed` method is an *event handler*. Event handlers are methods called by Textual in response to an *event* such as a key press, mouse click, etc.
Event handlers begin with `on_` followed by the name of the event they will handle.
Hence `on_button_pressed` will handle the button pressed event.

See the guide on [message handlers](./guide/events.md#message-handlers) for the details on how to write event handlers.

If you run `stopwatch04.py` now you will be able to toggle between the two states by clicking the first button:

```{.textual path="docs/examples/tutorial/stopwatch04.py" title="stopwatch04.py" press="tab,tab,tab,enter"}
```

When the button event handler adds or removes the `"started"` CSS class, Textual re-applies the CSS and updates the visuals.


## Reactive attributes

A recurring theme in Textual is that you rarely need to explicitly update a widget's visuals.
It is possible: you can call [refresh()][textual.widget.Widget.refresh] to display new data.
However, Textual prefers to do this automatically via _reactive_ attributes.

Reactive attributes work like any other attribute, such as those you might set in an `__init__` method, but allow Textual to detect when you assign to them, in addition to some other [*superpowers*](./guide/reactivity.md).

To add a reactive attribute, import [reactive][textual.reactive.reactive] and create an instance in your class scope.

Let's add reactives to our stopwatch to calculate and display the elapsed time.

```python title="stopwatch05.py" hl_lines="1 5 12-27 45"
--8<-- "docs/examples/tutorial/stopwatch05.py"
```

We have added two reactive attributes to the `TimeDisplay` widget: `start_time` will contain the time the stopwatch was started (in seconds), and `time` will contain the time to be displayed in the `Stopwatch` widget.

Both attributes will be available on `self` as if you had assigned them in `__init__`.
If you write to either of these attributes the widget will update automatically.

!!! info

    The `monotonic` function in this example is imported from the standard library `time` module.
    It is similar to `time.time` but won't go backwards if the system clock is changed.

The first argument to `reactive` may be a default value for the attribute or a callable that returns a default value.
We set the default for `start_time` to the `monotonic` function which will be called to initialize the attribute with the current time when the `TimeDisplay` is added to the app.
The `time` attribute has a simple float as the default, so `self.time` will be initialized to `0`.


The `on_mount` method is an event handler called when the widget is first added to the application (or _mounted_ in Textual terminology). In this method we call [set_interval()][textual.message_pump.MessagePump.set_interval] to create a timer which calls `self.update_time` sixty times a second. This `update_time` method calculates the time elapsed since the widget started and assigns it to `self.time` &mdash; which brings us to one of Reactive's super-powers.

If you implement a method that begins with `watch_` followed by the name of a reactive attribute, then the method will be called when the attribute is modified.
Such methods are known as *watch methods*.

Because `watch_time` watches the `time` attribute, when we update `self.time` 60 times a second we also implicitly call `watch_time` which converts the elapsed time to a string and updates the widget with a call to `self.update`.
Because this happens automatically, we don't need to pass in an initial argument to `TimeDisplay`.

The end result is that the `Stopwatch` widgets show the time elapsed since the widget was created:

```{.textual path="docs/examples/tutorial/stopwatch05.py" title="stopwatch05.py"}
```

We've seen how we can update widgets with a timer, but we still need to wire up the buttons so we can operate stopwatches independently.

### Wiring buttons

We need to be able to start, stop, and reset each stopwatch independently. We can do this by adding a few more methods to the `TimeDisplay` class.


```python title="stopwatch06.py" hl_lines="14 18 22 30-44 50-61"
--8<-- "docs/examples/tutorial/stopwatch06.py"
```

Here's a summary of the changes made to `TimeDisplay`.

- We've added a `total` reactive attribute to store the total time elapsed between clicking the start and stop buttons.
- The call to `set_interval` has grown a `pause=True` argument which starts the timer in pause mode (when a timer is paused it won't run until [resume()][textual.timer.Timer.resume] is called). This is because we don't want the time to update until the user hits the start button.
- The `update_time` method now adds `total` to the current time to account for the time between any previous clicks of the start and stop buttons.
- We've stored the result of `set_interval` which returns a [Timer](textual.timer.Timer) object. We will use this to _resume_ the timer when we start the Stopwatch.
- We've added `start()`, `stop()`, and `reset()` methods.

In addition, the `on_button_pressed` method on `Stopwatch` has grown some code to manage the time display when the user clicks a button. Let's look at that in detail:

```python
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        button_id = event.button.id
        time_display = self.query_one(TimeDisplay)
        if button_id == "start":
            time_display.start()
            self.add_class("started")
        elif button_id == "stop":
            time_display.stop()
            self.remove_class("started")
        elif button_id == "reset":
            time_display.reset()
```

This code supplies missing features and makes our app useful. We've made the following changes.

- The first line retrieves `id` attribute of the button that was pressed. We can use this to decide what to do in response.
- The second line calls [`query_one`][textual.dom.DOMNode.query_one] to get a reference to the `TimeDisplay` widget.
- We call the method on `TimeDisplay` that matches the pressed button.
- We add the `"started"` class when the Stopwatch is started (`self.add_class("started")`), and remove it (`self.remove_class("started")`) when it is stopped. This will update the Stopwatch visuals via CSS.

If you run `stopwatch06.py` you will be able to use the stopwatches independently.

```{.textual path="docs/examples/tutorial/stopwatch06.py" title="stopwatch06.py" press="tab,enter,tab,enter,tab"}
```

The only remaining feature of the Stopwatch app left to implement is the ability to add and remove stopwatches.

## Dynamic widgets

The Stopwatch app creates widgets when it starts via the `compose` method. We will also need to create new widgets while the app is running, and remove widgets we no longer need. We can do this by calling [mount()][textual.widget.Widget.mount] to add a widget, and [remove()][textual.widget.Widget.remove] to remove a widget.

Let's use these methods to implement adding and removing stopwatches to our app.

```python title="stopwatch.py" hl_lines="78-79 86 88-92 94-98"
--8<-- "docs/examples/tutorial/stopwatch.py"
```

Here's a summary of the changes:

- The `VerticalScroll` object in `StopWatchApp` grew a `"timers"` ID.
- Added `action_add_stopwatch` to add a new stopwatch.
- Added `action_remove_stopwatch` to remove a stopwatch.
- Added keybindings for the actions.

The `action_add_stopwatch` method creates and mounts a new stopwatch. Note the call to [query_one()][textual.dom.DOMNode.query_one] with a CSS selector of `"#timers"` which gets the timer's container via its ID.
Once mounted, the new Stopwatch will appear in the terminal. That last line in `action_add_stopwatch` calls [scroll_visible()][textual.widget.Widget.scroll_visible] which will scroll the container to make the new `Stopwatch` visible (if required).

The `action_remove_stopwatch` function calls [query()][textual.dom.DOMNode.query] with a CSS selector of `"Stopwatch"` which gets all the `Stopwatch` widgets.
If there are stopwatches then the action calls [last()][textual.css.query.DOMQuery.last] to get the last stopwatch, and [remove()][textual.css.query.DOMQuery.remove] to remove it.

If you run `stopwatch.py` now you can add a new stopwatch with the ++a++ key and remove a stopwatch with ++r++.

```{.textual path="docs/examples/tutorial/stopwatch.py" title="stopwatch.py" press="d,a,a,a,a,a,a,a,tab,enter,tab"}
```

## What next?

Congratulations on building your first Textual application! This tutorial has covered a lot of ground. If you are the type that prefers to learn a framework by coding, feel free. You could tweak `stopwatch.py` or look through the examples.

Read the guide for the full details on how to build sophisticated TUI applications with Textual.



================================================
FILE: docs/widget_gallery.md
================================================
---
hide:
  - navigation
---

# Widgets

Welcome to the Textual widget gallery.

We have many more widgets planned, or you can [build your own](./guide/widgets.md).


!!! info

    Textual is a **TUI** framework. Everything below runs in the *terminal*.


## Button

A simple button with a variety of semantic styles.

[Button reference](./widgets/button.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/button.py" columns="100" lines="24"}
```


## Checkbox

A classic checkbox control.

[Checkbox reference](./widgets/checkbox.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/checkbox.py"}
```


## Collapsible

Content that may be toggled on and off by clicking a title.

[Collapsible reference](./widgets/collapsible.md){ .md-button .md-button--primary }


```{.textual path="docs/examples/widgets/collapsible.py"}
```


## ContentSwitcher

A widget for containing and switching display between multiple child
widgets.

[ContentSwitcher reference](./widgets/content_switcher.md){ .md-button .md-button--primary }


## DataTable

A powerful data table, with configurable cursors.

[DataTable reference](./widgets/data_table.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/data_table.py"}
```

## Digits

Display numbers in tall characters.

[Digits reference](./widgets/digits.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/digits.py"}
```

## DirectoryTree

A tree view of files and folders.

[DirectoryTree reference](./widgets/directory_tree.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/directory_tree.py"}
```

## Footer

A footer to display and interact with key bindings.

[Footer reference](./widgets/footer.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/footer.py" columns="70" lines="12"}
```



## Header

A header to display the app's title and subtitle.


[Header reference](./widgets/header.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/header.py" columns="70" lines="12"}
```


## Input

A control to enter text.

[Input reference](./widgets/input.md){ .md-button .md-button--primary }


```{.textual path="docs/examples/widgets/input.py" press="D,a,r,r,e,n"}
```


## Label

A simple text label.

[Label reference](./widgets/label.md){ .md-button .md-button--primary }


## Link

A clickable link that opens a URL.

[Link reference](./widgets/link.md){ .md-button .md-button--primary }


## ListView

Display a list of items (items may be other widgets).

[ListView reference](./widgets/list_view.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/list_view.py"}
```

## LoadingIndicator

Display an animation while data is loading.

[LoadingIndicator reference](./widgets/loading_indicator.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/loading_indicator.py"}
```

## Log

Display and update lines of text (such as from a file).

[Log reference](./widgets/log.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/log.py"}
```

## MarkdownViewer

Display and interact with a Markdown document (adds a table of contents and browser-like navigation to Markdown).

[MarkdownViewer reference](./widgets/markdown_viewer.md){ .md-button .md-button--primary }


```{.textual path="docs/examples/widgets/markdown_viewer.py" columns="120" lines="50" press="tab,down"}
```

## Markdown

Display a markdown document.

[Markdown reference](./widgets/markdown.md){ .md-button .md-button--primary }


```{.textual path="docs/examples/widgets/markdown.py" columns="120" lines="53"}
```

## MaskedInput

A control to enter input according to a template mask.

[MaskedInput reference](./widgets/masked_input.md){ .md-button .md-button--primary }


```{.textual path="docs/examples/widgets/masked_input.py"}
```

## OptionList

Display a vertical list of options (options may be Rich renderables).

[OptionList reference](./widgets/option_list.md){ .md-button .md-button--primary }


```{.textual path="docs/examples/widgets/option_list_options.py"}
```

## Placeholder

Display placeholder content while you are designing a UI.

[Placeholder reference](./widgets/placeholder.md){ .md-button .md-button--primary }


```{.textual path="docs/examples/widgets/placeholder.py"}
```

## Pretty

Display a pretty-formatted Rich renderable.

[Pretty reference](./widgets/pretty.md){ .md-button .md-button--primary }


```{.textual path="docs/examples/widgets/pretty.py"}
```

## ProgressBar

A configurable progress bar with ETA and percentage complete.

[ProgressBar reference](./widgets/progress_bar.md){ .md-button .md-button--primary }


```{.textual path="docs/examples/widgets/progress_bar.py" press="5,0,tab,enter"}
```


## RadioButton

A simple radio button.

[RadioButton reference](./widgets/radiobutton.md){ .md-button .md-button--primary }


```{.textual path="docs/examples/widgets/radio_button.py"}
```

## RadioSet

A collection of radio buttons, that enforces uniqueness.

[RadioSet reference](./widgets/radioset.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/radio_set.py"}
```

## RichLog

Display and update text in a scrolling panel.

[RichLog reference](./widgets/rich_log.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/rich_log.py" press="H,i"}
```

## Rule

A rule widget to separate content, similar to a `<hr>` HTML tag.

[Rule reference](./widgets/rule.md){ .md-button .md-button--primary }


```{.textual path="docs/examples/widgets/horizontal_rules.py"}
```

## Select

Select from a number of possible options.

[Select reference](./widgets/select.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/select_widget.py" press="tab,enter,down,down"}
```

## SelectionList

Select multiple values from a list of options.

[SelectionList reference](./widgets/selection_list.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/selection_list_selections.py" press="down,down,down"}
```

## Sparkline

Display numerical data.

[Sparkline reference](./widgets/sparkline.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/sparkline.py" lines="11"}
```

## Static

Displays simple static content. Typically used as a base class.

[Static reference](./widgets/static.md){ .md-button .md-button--primary }


## Switch

An on / off control, inspired by toggle buttons.

[Switch reference](./widgets/switch.md){ .md-button .md-button--primary }


```{.textual path="docs/examples/widgets/switch.py"}
```

## Tabs

A row of tabs you can select with the mouse or navigate with keys.

[Tabs reference](./widgets/tabs.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/tabs.py" press="a,a,a,a,right,right"}
```

## TabbedContent

A Combination of Tabs and ContentSwitcher to navigate static content.

[TabbedContent reference](./widgets/tabbed_content.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/tabbed_content.py" press="j"}
```

## TextArea

A multi-line text area which supports syntax highlighting various languages.

[TextArea reference](./widgets/text_area.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/text_area_example.py" columns="42" lines="8"}
```

## Tree

A tree control with expandable nodes.

[Tree reference](./widgets/tree.md){ .md-button .md-button--primary }

```{.textual path="docs/examples/widgets/tree.py"}
```



================================================
FILE: docs/api/app.md
================================================
---
title: "textual.app"
---

::: textual.app
    options:
        filters:
          - "!^_"
          - "^__init__$"



================================================
FILE: docs/api/await_complete.md
================================================
---
title: "textual.await_complete"
---

This module contains the `AwaitComplete` class.
An `AwaitComplete` object is returned by methods that do work in the *background*.
You can await this object if you need to know when that work has completed.
Or you can ignore it, and Textual will automatically await the work before handling the next message.

!!! note

    You are unlikely to need to explicitly create these objects yourself.


::: textual.await_complete



================================================
FILE: docs/api/await_remove.md
================================================
---
title: "textual.await_remove"
---

This module contains the `AwaitRemove` class.
An `AwaitRemove` object is returned by [`Widget.remove()`][textual.widget.Widget.remove] and other methods which remove widgets.
You can await the return value if you need to know exactly when the widget(s) have been removed.
Or you can ignore it and Textual will wait for the widgets to be removed before handling the next message.

!!! note

    You are unlikely to need to explicitly create these objects yourself.


::: textual.await_remove



================================================
FILE: docs/api/binding.md
================================================
---
title: "textual.binding"
---

::: textual.binding



================================================
FILE: docs/api/cache.md
================================================
---
title: "textual.cache"
---

::: textual.cache



================================================
FILE: docs/api/color.md
================================================
---
title: "textual.color"
---

::: textual.color



================================================
FILE: docs/api/command.md
================================================
---
title: "textual.command"
---

::: textual.command



================================================
FILE: docs/api/compose.md
================================================
---
title: "textual.compose"
---

::: textual.compose.compose



================================================
FILE: docs/api/constants.md
================================================
---
title: "textual.constants"
---

::: textual.constants



================================================
FILE: docs/api/containers.md
================================================
---
title: "textual.containers"
---


::: textual.containers



================================================
FILE: docs/api/content.md
================================================
---
title: "textual.content"
---

::: textual.content



================================================
FILE: docs/api/coordinate.md
================================================
---
title: "textual.coordinate"
---


::: textual.coordinate



================================================
FILE: docs/api/dom_node.md
================================================
---
title: "textual.dom"
---

::: textual.dom



================================================
FILE: docs/api/errors.md
================================================
---
title: "textual.errors"
---

::: textual.errors



================================================
FILE: docs/api/events.md
================================================
---
title: "textual.events"
---


::: textual.events



================================================
FILE: docs/api/filter.md
================================================
---
title: "textual.filter"
---


::: textual.filter



================================================
FILE: docs/api/fuzzy_matcher.md
================================================
---
title: "textual.fuzzy"
---


::: textual.fuzzy



================================================
FILE: docs/api/geometry.md
================================================
---
title: "textual.geometry"
---


::: textual.geometry



================================================
FILE: docs/api/getters.md
================================================
---
title: "textual.getters"
---

::: textual.getters



================================================
FILE: docs/api/highlight.md
================================================
---
title: "textual.highlight"
---

::: textual.highlight



================================================
FILE: docs/api/index.md
================================================
# API

This is a API-level reference to the Textual API. Click the links to your left (or in the :octicons-three-bars-16: menu) to open a reference for each module.

If you are new to Textual, you may want to read the [tutorial](./../tutorial.md) or [guide](../guide/index.md) first.



================================================
FILE: docs/api/layout.md
================================================
---
title: "textual.layout"
---


::: textual.layout



================================================
FILE: docs/api/lazy.md
================================================
---
title: "textual.lazy"
---


::: textual.lazy



================================================
FILE: docs/api/logger.md
================================================
---
title: "textual"
---


::: textual



================================================
FILE: docs/api/logging.md
================================================
---
title: "textual.logging"
---
::: textual.logging



================================================
FILE: docs/api/map_geometry.md
================================================
---
title: "textual.map_geometry"
---


A data structure returned by [screen.find_widget][textual.screen.Screen.find_widget].

::: textual.map_geometry



================================================
FILE: docs/api/markup.md
================================================
---
title: "textual.markup"
---

::: textual.markup



================================================
FILE: docs/api/message.md
================================================
---
title: "textual.message"
---

::: textual.message



================================================
FILE: docs/api/message_pump.md
================================================
---
title: "textual.message_pump"
---

::: textual.message_pump



================================================
FILE: docs/api/on.md
================================================
---
title: "textual.on"
---

# On

::: textual.on



================================================
FILE: docs/api/pilot.md
================================================
---
title: "textual.pilot"
---

::: textual.pilot



================================================
FILE: docs/api/query.md
================================================
---
title: "textual.css.query"
---

::: textual.css.query



================================================
FILE: docs/api/reactive.md
================================================
---
title: "textual.reactive"
---

::: textual.reactive



================================================
FILE: docs/api/renderables.md
================================================
---
title: "textual.renderables"
---

A collection of Rich renderables which may be returned from a widget's [`render()`][textual.widget.Widget.render] method.

::: textual.renderables.bar
::: textual.renderables.blank
::: textual.renderables.digits
::: textual.renderables.gradient
::: textual.renderables.sparkline



================================================
FILE: docs/api/screen.md
================================================
---
title: "textual.screen"
---


::: textual.screen



================================================
FILE: docs/api/scroll_view.md
================================================
---
title: "textual.scroll_view"
---


::: textual.scroll_view



================================================
FILE: docs/api/scrollbar.md
================================================
---
title: "textual.scrollbar"
---

::: textual.scrollbar



================================================
FILE: docs/api/signal.md
================================================
---
title: "textual.signal"
---

::: textual.signal



================================================
FILE: docs/api/strip.md
================================================
---
title: "textual.strip"
---


::: textual.strip



================================================
FILE: docs/api/style.md
================================================
---
title: "textual.style"
---

::: textual.style



================================================
FILE: docs/api/suggester.md
================================================
---
title: "textual.suggester"
---


::: textual.suggester



================================================
FILE: docs/api/system_commands_source.md
================================================
---
title: "textual.system_commands"
---



::: textual.system_commands



================================================
FILE: docs/api/timer.md
================================================
---
title: "textual.timer"
---

::: textual.timer



================================================
FILE: docs/api/types.md
================================================
---
title: "textual.types"
---


::: textual.types



================================================
FILE: docs/api/validation.md
================================================
---
title: "textual.validation"
---


::: textual.validation



================================================
FILE: docs/api/walk.md
================================================
---
title: "textual.walk"
---


::: textual.walk



================================================
FILE: docs/api/widget.md
================================================
---
title: "textual.widget"
---


::: textual.widget
    options:
        filters:
          - "!^_"
          - "^__init__$"



================================================
FILE: docs/api/work.md
================================================
---
title: "textual.work"
---


::: textual.work



================================================
FILE: docs/api/worker.md
================================================
---
title: "textual.worker"
---

::: textual.worker



================================================
FILE: docs/api/worker_manager.md
================================================
---
title: "textual.worker_manager"
---

::: textual.worker_manager



================================================
FILE: docs/blog/index.md
================================================
# Textual Blog




================================================
FILE: docs/blog/.authors.yml
================================================
authors:
  willmcgugan:
    name: Will McGugan
    description: CEO / code-monkey
    avatar: https://github.com/willmcgugan.png
  darrenburns:
    name: Darren Burns
    description: Code-monkey
    avatar: https://github.com/darrenburns.png
  davep:
    name: Dave Pearson
    description: Code-monkey
    avatar: https://github.com/davep.png
  rodrigo:
    name: Rodrigo Girão Serrão
    description: Code-monkey
    avatar: https://github.com/rodrigogiraoserrao.png



================================================
FILE: docs/blog/posts/anatomy-of-a-textual-user-interface.md
================================================
---
draft: false
date: 2024-09-15
categories:
  - DevLog
authors:
  - willmcgugan
---

# Anatomy of a Textual User Interface

!!! note "My bad 🤦"

    The date is wrong on this post&mdash;it was actually published on the 2nd of September 2024.
    I don't want to fix it, as that would break the URL.

I recently wrote a [TUI](https://en.wikipedia.org/wiki/Text-based_user_interface) to chat to an AI agent in the terminal.
I'm not the first to do this (shout out to [Elia](https://github.com/darrenburns/elia) and [Paita](https://github.com/villekr/paita)), but I *may* be the first to have it reply as if it were the AI from the Aliens movies?

Here's a video of it in action:



<iframe width="100%" style="aspect-ratio:1512 / 982"  src="https://www.youtube.com/embed/hr5JvQS4d_w" title="Mother AI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Now let's dissect the code like Bishop dissects a facehugger.

<!-- more -->

## All right, sweethearts, what are you waiting for? Breakfast in bed?

At the top of the file we have some boilerplate:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "llm",
#     "textual",
# ]
# ///
from textual import on, work
from textual.app import App, ComposeResult
from textual.widgets import Header, Input, Footer, Markdown
from textual.containers import VerticalScroll
import llm

SYSTEM = """Formulate all responses as if you where the sentient AI named Mother from the Aliens movies."""
```

The text in the comment is a relatively new addition to the Python ecosystem.
It allows you to specify dependencies inline so that tools can setup an environment automatically.
The format of the comment was developed by [Ofek Lev](https://github.com/ofek) and first implemented in [Hatch](https://hatch.pypa.io/latest/blog/2024/05/02/hatch-v1100/#python-script-runner), and has since become a Python standard via [PEP 0723](https://peps.python.org/pep-0723/) (also authored by Ofek).

!!! note

    PEP 0723 is also implemented in [uv](https://docs.astral.sh/uv/guides/scripts/#running-scripts).

I really like this addition to Python because it means I can now share a Python script without the recipient needing to manually setup a fresh environment and install dependencies.

After this comment we have a bunch of imports: [textual](https://github.com/textualize/textual) for the UI, and [llm](https://llm.datasette.io/en/stable/) to talk to ChatGPT (also supports other LLMs).

Finally, we define `SYSTEM`, which is the *system prompt* for the LLM.

## Look, those two specimens are worth millions to the bio-weapons division.

Next up we have the following:

```python

class Prompt(Markdown):
    pass


class Response(Markdown):
    BORDER_TITLE = "Mother"
```

These two classes define the widgets which will display text the user enters and the response from the LLM.
They both extend the builtin [Markdown](https://textual.textualize.io/widgets/markdown/) widget, since LLMs like to talk in that format.

## Well, somebody's gonna have to go out there. Take a portable terminal, go out there and patch in manually.

Following on from the widgets we have the following:

```python
class MotherApp(App):
    AUTO_FOCUS = "Input"

    CSS = """
    Prompt {
        background: $primary 10%;
        color: $text;
        margin: 1;
        margin-right: 8;
        padding: 1 2 0 2;
    }

    Response {
        border: wide $success;
        background: $success 10%;
        color: $text;
        margin: 1;
        margin-left: 8;
        padding: 1 2 0 2;
    }
    """
```

This defines an app, which is the top-level object for any Textual app.

The `AUTO_FOCUS` string is a classvar which causes a particular widget to receive input focus when the app starts. In this case it is the `Input` widget, which we will define later.

The classvar is followed by a string containing CSS.
Technically, TCSS or *Textual Cascading Style Sheets*, a variant of CSS for terminal interfaces.

This isn't a tutorial, so I'm not going to go in to a details, but we're essentially setting properties on widgets which define how they look.
Here I styled the prompt and response widgets to have a different color, and tried to give the response a retro tech look with a green background and border.

We could express these styles in code.
Something like this:

```python
self.styles.color = "red"
self.styles.margin = 8
```

Which is fine, but CSS shines when the UI get's more complex.

## Look, man. I only need to know one thing: where they are.

After the app constants, we have a method called `compose`:

```python
    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(id="chat-view"):
            yield Response("INTERFACE 2037 READY FOR INQUIRY")
        yield Input(placeholder="How can I help you?")
        yield Footer()
```

This method adds the initial widgets to the UI.

`Header` and `Footer` are builtin widgets.

Sandwiched between them is a `VerticalScroll` *container* widget, which automatically adds a scrollbar (if required). It is pre-populated with a single `Response` widget to show a welcome message (the `with` syntax places a widget within a parent widget). Below that is an `Input` widget where we can enter text for the LLM.

This is all we need to define the *layout* of the TUI.
In Textual the layout is defined with styles (in the same was as color and margin).
Virtually any layout is possible, and you never have to do any math to calculate sizes of widgets&mdash;it is all done declaratively.

We could add a little CSS to tweak the layout, but the defaults work well here.
The header and footer are *docked* to an appropriate edge.
The `VerticalScroll` widget is styled to consume any available space, leaving room for widgets with a defined height (like our `Input`).

If you resize the terminal it will keep those relative proportions.

## Look into my eye.

The next method is an *event handler*.


```python
    def on_mount(self) -> None:
        self.model = llm.get_model("gpt-4o")
```

This method is called when the app receives a Mount event, which is one of the first events sent and is typically used for any setup operations.

It gets a `Model` object got our LLM of choice, which we will use later.

Note that the [llm](https://llm.datasette.io/en/stable/) library supports a [large number of models](https://llm.datasette.io/en/stable/openai-models.html), so feel free to replace the string with the model of your choice.

## We're in the pipe, five by five.

The next method is also a message handler:

```python
    @on(Input.Submitted)
    async def on_input(self, event: Input.Submitted) -> None:
        chat_view = self.query_one("#chat-view")
        event.input.clear()
        await chat_view.mount(Prompt(event.value))
        await chat_view.mount(response := Response())
        response.anchor()
        self.send_prompt(event.value, response)
```

The decorator tells Textual to handle the `Input.Submitted` event, which is sent when the user hits return in the Input.

!!! info "More on event handlers"

    There are two ways to receive events in Textual: a naming convention or the decorator.
    They aren't on the base class because the app and widgets can receive arbitrary events.

When that happens, this method clears the input and adds the prompt text to the `VerticalScroll`.
It also adds a `Response` widget to contain the LLM's response, and *anchors* it.
Anchoring a widget will keep it at the bottom of a scrollable view, which is just what we need for a chat interface.

Finally in that method we call `send_prompt`.

## We're on an express elevator to hell, going down!

Here is `send_prompt`:

```python
    @work(thread=True)
    def send_prompt(self, prompt: str, response: Response) -> None:
        response_content = ""
        llm_response = self.model.prompt(prompt, system=SYSTEM)
        for chunk in llm_response:
            response_content += chunk
            self.call_from_thread(response.update, response_content)
```

You'll notice that it is decorated with `@work`, which turns this method in to a *worker*.
In this case, a *threaded* worker. Workers are a layer over async and threads, which takes some of the pain out of concurrency.

This worker is responsible for sending the prompt, and then reading the response piece-by-piece.
It calls the Markdown widget's `update` method which replaces its content with new Markdown code, to give that funky streaming text effect.


## Game over man, game over!

The last few lines creates an app instance and runs it:

```python
if __name__ == "__main__":
    app = MotherApp()
    app.run()
```

You may need to have your [API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) set in an environment variable.
Or if you prefer, you could set in the `on_mount` function with the following:

```python
self.model.key = "... key here ..."
```

## Not bad, for a human.

Here's the [code for the Mother AI](https://gist.github.com/willmcgugan/648a537c9d47dafa59cb8ece281d8c2c).

Run the following in your shell of choice to launch mother.py (assumes you have [uv](https://docs.astral.sh/uv/) installed):

```base
uv run mother.py
```

## You know, we manufacture those, by the way.

Join our [Discord server](https://discord.gg/Enf6Z3qhVr) to discuss more 80s movies (or possibly TUIs).



================================================
FILE: docs/blog/posts/await-me-maybe.md
================================================
---
draft: false
date: 2023-03-15
categories:
  - DevLog
authors:
  - willmcgugan
---

# No-async async with Python

A (reasonable) criticism of async is that it tends to proliferate in your code. In order to `await` something, your functions must be `async` all the way up the call-stack. This tends to result in you making things `async` just to support that one call that needs it or, worse, adding `async` just-in-case. Given that going from `def` to `async def` is a breaking change there is a strong incentive to go straight there.

Before you know it, you have adopted a policy of "async all the things".

<!-- more -->

Textual is an async framework, but doesn't *require* the app developer to use the `async` and `await` keywords (but you can if you need to). This post is about how Textual accomplishes this async-agnosticism.

!!! info

    See this [example](https://textual.textualize.io/guide/widgets/#attributes-down) from the docs for an async-less Textual app.


## An apology

But first, an apology! In a previous post I said Textual "doesn't do any IO of its own". This is not accurate. Textual responds to keys and mouse events (**I**nput) and writes content to the terminal (**O**utput).

Although Textual clearly does do IO, it uses `asyncio` mainly for *concurrency*. It allows each widget to update its part of the screen independently from the rest of the app.

## Await me (maybe)

The first no-async async technique is the "Await me maybe" pattern, a term first coined by [Simon Willison](https://simonwillison.net/2020/Sep/2/await-me-maybe/). This is particularly applicable to callbacks (or in Textual terms, message handlers).

The `await_me_maybe` function below can run a callback that is either a plain old function *or* a coroutine (`async def`). It does this by awaiting the result of the callback if it is awaitable, or simply returning the result if it is not.


```python
import asyncio
import inspect


def plain_old_function():
    return "Plain old function"

async def async_function():
    return "Async function"


async def await_me_maybe(callback):
    result = callback()
    if inspect.isawaitable(result):
        return await result
    return result


async def run_framework():
    print(
        await await_me_maybe(plain_old_function)
    )
    print(
        await await_me_maybe(async_function)
    )


if __name__ == "__main__":
    asyncio.run(run_framework())
```

## Optionally awaitable

The "await me maybe" pattern is great when an async framework calls the app's code. The app developer can choose to write async code or not. Things get a little more complicated when the app wants to call the framework's API. If the API has *asynced all the things*, then it would force the app to do the same.

Textual's API consists of regular methods for the most part, but there are a few methods which are optionally awaitable. These are *not* coroutines (which must be awaited to do anything).

In practice, this means that those API calls initiate something which will complete a short time later. If you discard the return value then it won't prevent it from working. You only need to `await` if you want to know when it has finished.

The `mount` method is one such method. Calling it will add a widget to the screen:

```python
def on_key(self):
    # Add MyWidget to the screen
    self.mount(MyWidget("Hello, World!"))
```

In this example we don't care that the widget hasn't been mounted immediately, only that it will be soon.

!!! note

    Textual awaits the result of mount after the message handler, so even if you don't *explicitly* await it, it will have been completed by the time the next message handler runs.

We might care if we want to mount a widget then make some changes to it. By making the handler `async` and awaiting the result of mount, we can be sure that the widget has been initialized before we update it:

```python
async def on_key(self):
    # Add MyWidget to the screen
    await self.mount(MyWidget("Hello, World!"))
    # add a border
    self.query_one(MyWidget).styles.border = ("heavy", "red")
```

Incidentally, I found there were very few examples of writing awaitable objects in Python. So here is the code for `AwaitMount` which is returned by the `mount` method:

```python
class AwaitMount:
    """An awaitable returned by mount() and mount_all()."""

    def __init__(self, parent: Widget, widgets: Sequence[Widget]) -> None:
        self._parent = parent
        self._widgets = widgets

    async def __call__(self) -> None:
        """Allows awaiting via a call operation."""
        await self

    def __await__(self) -> Generator[None, None, None]:
        async def await_mount() -> None:
            if self._widgets:
                aws = [
                    create_task(widget._mounted_event.wait(), name="await mount")
                    for widget in self._widgets
                ]
                if aws:
                    await wait(aws)
                    self._parent.refresh(layout=True)

        return await_mount().__await__()
```

## Summing up

Textual did initially "async all the things", which you might see if you find some old Textual code. Now async is optional.

This is not because I dislike async. I'm a fan! But it does place a small burden on the developer (more to type and think about). With the current API you generally don't need to write coroutines, or remember to await things. But async is there if you need it.

We're finding that Textual is increasingly becoming a UI to things which are naturally concurrent, so async was a good move. Concurrency can be a tricky subject, so we're planning some API magic to take the pain out of running tasks, threads, and processes. Stay tuned!

Join us on our [Discord server](https://discord.gg/Enf6Z3qhVr) if you want to talk about these things with the Textualize developers.



================================================
FILE: docs/blog/posts/be-the-keymaster.md
================================================
---
draft: false
date: 2022-12-08
categories:
  - DevLog
authors:
  - davep
---

# Be the Keymaster!

## That didn't go to plan

So... yeah... the blog. When I wrote [my previous (and first)
post](https://textual.textualize.io/blog/2022/11/26/on-dog-food-the-original-metaverse-and-not-being-bored/)
I had wanted to try and do a post towards the end of each week, highlighting
what I'd done on the "dogfooding" front. Life kinda had other plans. Not in
a terrible way, but it turns out that getting both flu and Covid jabs (AKA
"jags" as they tend to say in my adopted home) on the same day doesn't
really agree with me too well.

I *have* been working, but there's been some odd moments in the past week
and a bit and, last week, once I got to the end, I was glad for it to end.
So no blog post happened.

Anyway...

<!-- more -->

## What have I been up to?

While mostly sat feeling sorry for myself on my sofa, I have been coding.
Rather than list all the different things here in detail, I'll quickly
mention them with links to where to find them and play with them if you
want:

### FivePyFive

While my Textual 5x5 puzzle is [one of the examples in the Textual
repo](https://github.com/Textualize/textual/tree/main/examples), I wanted to
make it more widely available so people can download it with `pip` or
[`pipx`](https://pypa.github.io/pipx/). See [over on
PyPi](https://pypi.org/project/fivepyfive/) and see if you can solve it. ;-)

<div class="video-wrapper">
    <iframe
        width="560" height="315"
        src="https://www.youtube.com/embed/Rf34Z5r7Q60"
        title="PISpy" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
</div>

### textual-qrcode

I wanted to put together a very small example of how someone may put
together a third party widget library, and in doing so selected what I
thought was going to be a mostly-useless example: [a wrapper around a
text-based QR code generator
website](https://pypi.org/project/textual-qrcode/). Weirdly I've had a
couple of people express a need for QR codes in the terminal since
publishing that!

![A Textual QR Code](../images/2022-12-08-davep-devlog/textual-qrcode.png)

### PISpy

[PISpy](https://pypi.org/project/pispy-client/) is a very simple
terminal-based client for the [PyPi
API](https://warehouse.pypa.io/api-reference/). Mostly it provides a
hypertext interface to Python package details, letting you look up a package
and then follow its dependency links. It's *very* simple at the moment, but
I think more fun things can be done with this.

<div class="video-wrapper">
    <iframe
        width="560" height="315"
        src="https://www.youtube.com/embed/yMGD6bXqIEo"
        title="PISpy" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
</div>

### OIDIA

I'm a big fan of the use of streak-tracking in one form or another.
Personally I use a [streak-tracking app](https://streaksapp.com/) for
keeping tabs of all sorts of good (and bad) habits, and as a heavy user of
all things Apple I make a lot of use of [the Fitness
rings](https://www.apple.com/uk/watch/close-your-rings/), etc. So I got to
thinking it might be fun to do a really simple, no shaming, no counting,
just recording, steak app for the Terminal.
[OIDIA](https://pypi.org/project/oidia/) is the result.

<div class="video-wrapper">
    <iframe
        width="560" height="315"
        src="https://www.youtube.com/embed/3Kz8eUzO9-8"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
</div>

As of the time of writing I only finished the first version of this
yesterday evening, so there are plenty of rough edges; but having got it to
a point where it performed the basic tasks I wanted from it, that seemed
like a good time to publish.

Expect to see this getting more updates and polish.

## Wait, what about this Keymaster thing?

Ahh, yes, about that... So one of the handy things I'm finding about Textual
is its [key binding
system](https://textual.textualize.io/guide/input/#bindings). The more
I build Textual apps, the more I appreciate the bindings, how they can be
associated with specific widgets, the use of actions (which can be used from
other places too), etc.

But... (there's always a "but" right -- I mean, there'd be no blog post to
be had here otherwise).

The terminal doesn't have access to all the key combinations you may want to
use, and also, because some keys can't necessarily be "typed", at least not
easily (think about it: there's no <kbd>F1</kbd> character, you have to type
`F1`), many keys and key combinations need to be bound with specific names.

So there's two problems here: how do I discover what keys even turn up in my
application, and when they do, what should I call them when I pass them to
[`Binding`](https://textual.textualize.io/api/binding/#textual.binding.Binding)?

That felt like a *"well Dave just build an app for it!"* problem. So I did:

<div class="video-wrapper">
    <iframe
        width="560" height="315"
        src="https://www.youtube.com/embed/-MV8LFfEOZo"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
</div>

If you're building apps with Textual and you want to discover what keys turn
up from your terminal and are available to your application, you can:

```sh
$ pipx install textual-keys
```

and then just run `textual-keys` and start mashing the keyboard to find out.

There's a good chance that this app, or at least a version of it, will make
it into Textual itself (very likely as one of the
[devtools](https://textual.textualize.io/guide/devtools/)). But for now it's
just an easy install away.

I think there's a call to be made here too: have you built anything to help
speed up how you work with Textual, or just make the development experience
"just so"? If so, do let us know, and come yell about it on the
[`#show-and-tell`
channel](https://discord.com/channels/1026214085173461072/1033752599112994867)
in [our Discord server](https://discord.gg/Enf6Z3qhVr).



================================================
FILE: docs/blog/posts/better-sleep-on-windows.md
================================================
---
draft: false
date: 2022-12-30
categories:
  - DevLog
authors:
  - willmcgugan
---
# A better asyncio sleep for Windows to fix animation

I spent some time optimizing Textual on Windows recently, and discovered something which may be of interest to anyone working with async code on that platform.

<!-- more -->

Animation, scrolling, and fading had always been unsatisfactory on Windows. Textual was usable, but the lag when scrolling made apps feel far less snappy that other platforms. On macOS and Linux, scrolling is fast enough that it feels close to a native app, not something running in a terminal. Yet the Windows experience never improved, even as Textual got faster with each release.

I had chalked this up to Windows Terminal being slow to render updates. After all, the classic Windows terminal was (and still is) glacially slow. Perhaps Microsoft just weren't focusing on performance.

In retrospect, that was highly improbable. Like all modern terminals, Windows Terminal uses the GPU to render updates. Even without focussing on performance, it should be fast.

I figured I'd give it one last attempt to speed up Textual on Windows. If I failed, Windows would forever be a third-class platform for Textual apps.

It turned out that it was nothing to do with performance, per se. The issue was with a single asyncio function: `asyncio.sleep`.

Textual has a `Timer` class which creates events at regular intervals. It powers the JS-like `set_interval` and `set_timer` functions. It is also used internally to do animation (such as smooth scrolling). This Timer class calls `asyncio.sleep` to wait the time between one event and the next.

On macOS and Linux, calling `asynco.sleep` is fairly accurate. If you call `sleep(3.14)`, it will return within 1% of 3.14 seconds. This is not the case for Windows, which for historical reasons uses a timer with a granularity of 15 milliseconds. The upshot is that sleep times will be rounded up to the nearest multiple of 15 milliseconds.

This limit appears to hold true for all async primitives on Windows. If you wait for something with a timeout, it will return on a multiple of 15 milliseconds. Fortunately there is work in the CPython pipeline to make this more accurate. Thanks to [Steve Dower](https://twitter.com/zooba) for pointing this out.

This lack of accuracy in the timer meant that timer events were created at a far slower rate than intended. Animation was slower because Textual was waiting too long between updates.

Once I had figured that out, I needed an alternative to `asyncio.sleep` for Textual's Timer class. And I found one. The following version of `sleep` is accurate to well within 1%:

```python
from time import sleep as time_sleep
from asyncio import get_running_loop

async def sleep(sleep_for: float) -> None:
    """An asyncio sleep.

    On Windows this achieves a better granularity than asyncio.sleep

    Args:
        sleep_for (float): Seconds to sleep for.
    """
    await get_running_loop().run_in_executor(None, time_sleep, sleep_for)

```

That is a drop-in replacement for sleep on Windows. With it, Textual runs a *lot* smoother. Easily on par with macOS and Linux.

It's not quite perfect. There is a little *tearing* during full "screen" updates, but performance is decent all round. I suspect when [this bug]( https://bugs.python.org/issue37871) is fixed (big thanks to [Paul Moore](https://twitter.com/pf_moore) for looking in to that), and Microsoft implements [this protocol](https://gist.github.com/christianparpart/d8a62cc1ab659194337d73e399004036) then Textual on Windows will be A+.

This Windows improvement will be in v0.9.0 of [Textual](https://github.com/Textualize/textual), which will be released in a few days.



================================================
FILE: docs/blog/posts/create-task-psa.md
================================================
---
draft: false
date: 2023-02-11
categories:
  - DevLog
authors:
  - willmcgugan
---

# The Heisenbug lurking in your async code

I'm taking a brief break from blogging about [Textual](https://github.com/Textualize/textual) to bring you this brief PSA for Python developers who work with async code. I wanted to expand a little on this [tweet](https://twitter.com/willmcgugan/status/1624419352211603461).

<!-- more -->

If you have ever used `asyncio.create_task` you may have created a bug for yourself that is challenging (read *almost impossible*) to reproduce. If it occurs, your code will likely fail in unpredictable ways.

The root cause of this [Heisenbug](https://en.wikipedia.org/wiki/Heisenbug) is that if you don't hold a reference to the task object returned by `create_task` then the task may disappear without warning when Python runs garbage collection. In other words, the code in your task will stop running with no obvious indication why.

This behavior is [well documented](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task), as you can see from this excerpt (emphasis mine):

![create task](../images/async-create-task.jpeg)

But who reads all the docs? And who has perfect recall if they do? A search on GitHub indicates that there are a [lot of projects](https://github.com/search?q=%22asyncio.create_task%28%22&type=code) where this bug is waiting for just the right moment to ruin somebody's day.

I suspect the reason this mistake is so common is that tasks are a lot like threads (conceptually at least). With threads you can just launch them and forget. Unless you mark them as "daemon" threads they will exist for the lifetime of your app. Not so with Tasks.

The solution recommended in the docs is to keep a reference to the task for as long as you need it to live. On modern Python you could use [TaskGroups](https://docs.python.org/3/library/asyncio-task.html#task-groups) which will keep references to your tasks. As long as all the tasks you spin up are in TaskGroups, you should be fine.



================================================
FILE: docs/blog/posts/creating-tasks-overhead.md
================================================
---
draft: false
date: 2023-03-08
categories:
  - DevLog
authors:
  - willmcgugan
---

# Overhead of Python Asyncio tasks

Every widget in Textual, be it a button, tree view, or a text input, runs an [asyncio](https://docs.python.org/3/library/asyncio.html) task. There is even a task for [scrollbar corners](https://github.com/Textualize/textual/blob/e95a65fa56e5b19715180f9e17c7f6747ba15ec5/src/textual/scrollbar.py#L365) (the little space formed when horizontal and vertical scrollbars meet).

<!-- more -->

!!! info

    It may be IO that gives AsyncIO its name, but Textual doesn't do any IO of its own. Those tasks are used to power *message queues*, so that widgets (UI components) can do whatever they do at their own pace.

Its fair to say that Textual apps launch a lot of tasks. Which is why when I was trying to optimize startup (for apps with 1000s of widgets) I suspected it was task related.

I needed to know how much of an overhead it was to launch tasks. Tasks are lighter weight than threads, but how much lighter? The only way to know for certain was to profile.

The following code launches a load of *do nothing* tasks, then waits for them to shut down. This would give me an idea of how performant `create_task` is, and also a *baseline* for optimizations. I would know the absolute limit of any optimizations I make.

```python
from asyncio import create_task, wait, run
from time import process_time as time


async def time_tasks(count=100) -> float:
    """Time creating and destroying tasks."""

    async def nop_task() -> None:
        """Do nothing task."""
        pass

    start = time()
    tasks = [create_task(nop_task()) for _ in range(count)]
    await wait(tasks)
    elapsed = time() - start
    return elapsed


for count in range(100_000, 1000_000 + 1, 100_000):
    create_time = run(time_tasks(count))
    create_per_second = 1 / (create_time / count)
    print(f"{count:,} tasks \t {create_per_second:0,.0f} tasks per/s")
```

And here is the output:

```
100,000 tasks    280,003 tasks per/s
200,000 tasks    255,275 tasks per/s
300,000 tasks    248,713 tasks per/s
400,000 tasks    248,383 tasks per/s
500,000 tasks    241,624 tasks per/s
600,000 tasks    260,660 tasks per/s
700,000 tasks    244,510 tasks per/s
800,000 tasks    247,455 tasks per/s
900,000 tasks    242,744 tasks per/s
1,000,000 tasks          259,715 tasks per/s
```

!!! info

    Running on an M1 MacBook Pro.

This tells me I can create, run, and shutdown 260K tasks per second.

That's fast.

Clearly `create_task` is as close as you get to free in the Python world, and I would need to look elsewhere for optimizations. Turns out Textual spends far more time processing CSS rules than creating tasks (obvious in retrospect). I've noticed some big wins there, so the next version of Textual will be faster to start apps with a metric tonne of widgets.

But I still need to know what to do with those scrollbar corners. A task for two characters. I don't even...



================================================
FILE: docs/blog/posts/darren-year-in-review.md
================================================
---
draft: false
date: 2022-12-20
categories:
  - DevLog
authors:
  - darrenburns
---
# A year of building for the terminal

I joined Textualize back in January 2022, and since then have been hard at work with the team on both [Rich](https://github.com/Textualize/rich) and [Textual](https://github.com/Textualize/textual).
Over the course of the year, I’ve been able to work on a lot of really cool things.
In this post, I’ll review a subset of the more interesting and visual stuff I’ve built. If you’re into terminals and command line tooling, you’ll hopefully see at least one thing of interest!

<!-- more -->

## A file manager powered by Textual

I’ve been slowly developing a file manager as a “dogfooding” project for Textual. It takes inspiration from tools such as Ranger and Midnight Commander.

![Untitled](../images/darren-year-in-review/Untitled.png)

As of December 2022, it lets you browse your file system, filtering, multi-selection, creating and deleting files/directories, opening files in your `$EDITOR` and more.

I’m happy with how far this project has come — I think it’s a good example of the type of powerful application that can be built with Textual with relatively little code. I’ve been able to focus on *features*, instead of worrying about terminal emulator implementation details.

![filemanager-trimmed.gif](../images/darren-year-in-review/filemanager-trimmed.gif)

The project is available [on GitHub](https://github.com/darrenburns/kupo).

## Better diffs in the terminal

Diffs in the terminal are often difficult to read at a glance. I wanted to see how close I could get to achieving a diff display of a quality similar to that found in the GitHub UI.

To attempt this, I built a tool called [Dunk](https://github.com/darrenburns/dunk). It’s a command line program which you can pipe your `git diff` output into, and it’ll convert it into something which I find much more readable.

![Untitled](../images/darren-year-in-review/Untitled%201.png)

Although I’m not particularly proud of the code - there are a lot of “hacks” going on, but I’m proud of the result. If anything, it shows what can be achieved for tools like this.

For many diffs, the difference between running `git diff` and `git diff | dunk | less -R` is night and day.

![Untitled](../images/darren-year-in-review/Untitled%202.png)

It’d be interesting to revisit this at some point.
It has its issues, but I’d love to see how it can be used alongside Textual to build a terminal-based diff/merge tool. Perhaps it could be combined with…

## Code editor floating gutter

This is a common feature in text editors and IDEs: when you scroll to the right, you should still be able to see what line you’re on. Out of interest, I tried to recreate the effect in the terminal using Textual.

![floating-gutter.gif](../images/darren-year-in-review/floating-gutter.gif)

Textual CSS offers a `dock` property which allows you to attach a widget to an edge of its parent.
By creating a widget that contains a vertical list of numbers and setting the `dock` property to `left`, we can create a floating gutter effect.
Then, we just need to keep the `scroll_y` in sync between the gutter and the content to ensure the line numbers stay aligned.

## Dropdown autocompletion menu

While working on [Shira](https://github.com/darrenburns/shira) (a proof-of-concept, terminal-based Python object explorer), I wrote some autocompleting dropdown functionality.

![shira-demo.gif](../images/darren-year-in-review/shira-demo.gif)

Textual forgoes the z-index concept from browser CSS and instead uses a “named layer” system. Using the `layers` property you can defined an ordered list of named layers, and using the `layer` property, you can assign a descendant widget to one of those layers.

By creating a new layer above all others and assigning a widget to that layer, we can ensure that widget is painted above everything else.

In order to determine where to place the dropdown, we can track the current value in the dropdown by `watch`ing the reactive input “value” inside the Input widget. This method will be called every time the `value` of the Input changes, and we can use this hook to amend the position of our dropdown position to accommodate for the length of the input value.

![Untitled](../images/darren-year-in-review/Untitled%203.png)

I’ve now extracted this into a separate library called [textual-autocomplete](https://github.com/darrenburns/textual-autocomplete).

## Tabs with animated underline

The aim here was to create a tab widget with underlines that animates smoothly as another tab is selected.

<video style="position: relative; width: 100%;" controls autoplay loop><source src="../../../../images/darren-year-in-review/tabs-textual-video-demo.mp4" type="video/mp4"></video>

The difficulty with implementing something like this is that we don’t have pixel-perfect resolution when animating - a terminal window is just a big grid of fixed-width character cells.

![Untitled](../images/darren-year-in-review/Untitled%204.png){ align=right width=250 }
However, when animating things in a terminal, we can often achieve better granularity using Unicode related tricks. In this case, instead of shifting the bar along one whole cell, we adjust the endings of the bar to be a character which takes up half of a cell.

The exact characters that form the bar are "╺", "━" and "╸". When the bar sits perfectly within cell boundaries, every character is “━”. As it travels over a cell boundary, the left and right ends of the bar are updated to "╺" and "╸" respectively.

## Snapshot testing for terminal apps

One of the great features we added to Rich this year was the ability to export console contents to an SVG. This feature was later exposed to Textual, allowing users to capture screenshots of their running Textual apps.
Ultimately, I ended up creating a tool for snapshot testing in the Textual codebase.

Snapshot testing is used to ensure that Textual output doesn’t unexpectedly change. On disk, we store what we expect the output to look like. Then, when we run our unit tests, we get immediately alerted if the output has changed.

This essentially automates the process of manually spinning up several apps and inspecting them for unexpected visual changes. It’s great for catching subtle regressions!

In Textual, each CSS property has its own canonical example and an associated snapshot test.
If we accidentally break a property in a way that affects the visual output, the chances of it sneaking into a release are greatly reduced, because the corresponding snapshot test will fail.

As part of this work, I built a web interface for comparing snapshots with test output.
There’s even a little toggle which highlights the differences, since they’re sometimes rather subtle.

<video style="position: relative; width: 100%;" controls autoplay loop><source src="../../../../images/darren-year-in-review/Screen_Recording_2022-12-14_at_14.08.15.mov" type="video/mp4"></video>

Since the terminal output shown in the video above is just an SVG image, I was able to add the "Show difference" functionality
by overlaying the two images and applying a single CSS property: `mix-blend-mode: difference;`.

The snapshot testing functionality itself is implemented as a pytest plugin, and it builds on top of a snapshot testing framework called [syrupy](https://github.com/tophat/syrupy).

![Screenshot 2022-09-16 at 15.52.03.png](..%2Fimages%2Fdarren-year-in-review%2FScreenshot%202022-09-16%20at%2015.52.03.png)

It's quite likely that this will eventually be exposed to end-users of Textual.

## Demonstrating animation

I built an example app to demonstrate how to animate in Textual and the available easing functions.

<video style="position: relative; width: 100%;" controls loop><source src="../../../../images/darren-year-in-review/animation-easing-example.mov" type="video/mp4"></video>

The smoothness here is achieved using tricks similar to those used in the tabs I discussed earlier.
In fact, the bar that animates in the video above is the same Rich renderable that is used by Textual's scrollbars.

You can play with this app by running `textual easing`. Please use animation sparingly.

## Developer console

When developing terminal based applications, performing simple debugging using `print` can be difficult, since the terminal is in application mode.

A project I worked on earlier in the year to improve the situation was the Textual developer console, which you can launch with `textual console`.

<div>
<figure markdown>
    <img src="../../../../images/darren-year-in-review/devtools.png">
    <figcaption>On the right, <a href="https://twitter.com/davepdotorg">Dave's</a> 5x5 Textual app. On the left, the Textual console.</figcaption>
</figure>
</div>

Then, by running a Textual application with the `--dev` flag, all standard output will be redirected to it.
This means you can use the builtin `print` function and still immediately see the output.
Textual itself also writes information to this console, giving insight into the messages that are flowing through an application.

## Pixel art

Cells in the terminal are roughly two times taller than they are wide. This means, that two horizontally adjacent cells form an approximate square.

Using this fact, I wrote a simple library based on Rich and PIL which can convert an image file into terminal output.
You can find the library, `rich-pixels`, [on GitHub](https://github.com/darrenburns/rich-pixels).

It’s particularly good for displaying simple pixel art images. The SVG image below is also a good example of the SVG export functionality I touched on earlier.

<div>
--8<-- "docs/blog/images/darren-year-in-review/bulbasaur.svg"
</div>

Since the library generates an object which is renderable using Rich, these can easily be embedded inside Textual applications.

Here's an example of that in a scrapped "Pokédex" app I threw together:

<video style="position: relative; width: 100%;" controls autoplay loop><source src="../../../../images/darren-year-in-review/pokedex-terminal.mov" type="video/mp4"></video>

This is a rather naive approach to the problem... but I did it for fun!

Other methods for displaying images in the terminal include:

- A more advanced library like [chafa](https://github.com/hpjansson/chafa), which uses a range of Unicode characters to achieve a more accurate representation of the image.
- One of the available terminal image protocols, such as Sixel, Kitty’s Terminal Graphics Protocol, and iTerm Inline Images Protocol.

<hr>

That was a whirlwind tour of just some of the projects I tackled in 2022.
If you found it interesting, be sure to [follow me on Twitter](https://twitter.com/_darrenburns).
I don't post often, but when I do, it's usually about things similar to those I've discussed here.



================================================
FILE: docs/blog/posts/future-of-textualize.md
================================================
---
draft: false
date: 2025-05-07
title: "The future of Textualize"
categories:
  - News
authors:
  - willmcgugan
---

Textual has come a *long* way since I figured why not build an application framework on top of [Rich](https://github.com/Textualize/rich).

Both were initially hobby projects. I mean look how much fun I was having back then:

<!-- more -->

<blockquote class="twitter-tweet" data-media-max-width="560"><p lang="en" dir="ltr">Making good progress with Textual CSS. <br><br>Here&#39;s a &quot;basic&quot; app. The <a href="https://twitter.com/hashtag/Python?src=hash&amp;ref_src=twsrc%5Etfw">#Python</a> + CSS in the screenshots generates the layout in the terminal here.<br><br>Separating the layout and design from the runtime logic will make it easy to create gorgeous TUI apps. 🤩 <a href="https://t.co/Rxnwzs4pXd">pic.twitter.com/Rxnwzs4pXd</a></p>&mdash; Will McGugan (@willmcgugan) <a href="https://twitter.com/willmcgugan/status/1463977921891217411?ref_src=twsrc%5Etfw">November 25, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Working on Textual has been a constant source of delight; figuring out how to make a terminal do things that it shouldn't really be able to do, and to a lesser extent a source of frustration when working around the baffling edge cases in emulators and the terminal protocol.

But work around it we did, and now Textual is an awesome piece of software that has spawned a community of developers building TUIs for [all kinds of things](https://github.com/textualize/transcendent-textual) (not to mention, [web apps](https://github.com/Textualize/textual-serve))!

Additionally, Textual has some of the [best docs](https://textual.textualize.io/guide/screens/) for any Open Source project. Shout out to [@squidfunk](https://x.com/squidfunk) and [@pawamoy](https://x.com/pawamoy) for the tech that makes these beautiful docs possible.

Ultimately though a business needs a product. Textual has always been a solution in search of a problem. And while there are plenty of problems to which Textual is a fantastic solution, we weren't able to find a shared problem or pain-point to build a viable business around. Which is why Textualize, the company, will be wrapping up in the next few weeks.

Textual will live on as an Open Source project. In the near term, nothing much will change. I will be maintaining Textual and Rich as I have always done. Software is never finished, but Textual is mature and battle-tested. I'm confident transitioning from a full-time funded project to a community project won't have a negative impact.

## Thanks!

I'd like to thank the awesome devs I worked with at Textualize, and the many developers that followed along, contributing and building apps. Wether you were an early adopter or you just discovered Textual, you made Textual what it is today.

## Get in touch

If you would like to talk Textual, feel free to find me on our [Discord server](https://github.com/textualize/textual/) or the socials.

I've also started a [blog](https://willmcgugan.github.io/) where I will write a little more on this from a more personal perspective.



================================================
FILE: docs/blog/posts/helo-world.md
================================================
---
draft: false
date: 2022-11-06
categories:
  - News
authors:
  - willmcgugan
---

# New Blog

Welcome to the first post on the Textual blog.

<!-- more -->

I plan on using this as a place to make announcements regarding new releases of Textual, and any other relevant news.

The first piece of news is that we've reorganized this site a little. The Events, Styles, and Widgets references are now under "Reference", and what used to be under "Reference" is now "API" which contains API-level documentation. I hope that's a little clearer than it used to be!




================================================
FILE: docs/blog/posts/inline-mode.md
================================================
---
draft: false
date: 2024-04-20
categories:
  - DevLog
authors:
  - willmcgugan
---

# Behind the Curtain of Inline Terminal Applications

Textual recently added the ability to run *inline* terminal apps.
You can see this in action if you run the [calculator example](https://github.com/Textualize/textual/blob/main/examples/calculator.py):

![Inline Calculator](../images/calcinline.png)

The application appears directly under the prompt, rather than occupying the full height of the screen&mdash;which is more typical of TUI applications.
You can interact with this calculator using keys *or* the mouse.
When you press ++ctrl+q++ the calculator disappears and returns you to the prompt.

Here's another app that creates an inline code editor:

=== "Video"

    <div class="video-wrapper">
        <iframe width="852" height="525" src="https://www.youtube.com/embed/Dt70oSID1DY" title="Inline app" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>


=== "inline.py"
    ```python
    from textual.app import App, ComposeResult
    from textual.widgets import TextArea


    class InlineApp(App):
        CSS = """
        TextArea {
            height: auto;
            max-height: 50vh;
        }
        """

        def compose(self) -> ComposeResult:
            yield TextArea(language="python")


    if __name__ == "__main__":
        InlineApp().run(inline=True)

    ```

This post will cover some of what goes on under the hood to make such inline apps work.

It's not going to go in to too much detail.
I'm assuming most readers will be more interested in a birds-eye view rather than all the gory details.

<!-- more -->

## Programming the terminal

Firstly, let's recap how you program the terminal.
Broadly speaking, the terminal is a device for displaying text.
You write (or print) text to the terminal which typically appears at the end of a continually growing text buffer.
In addition to text you can also send [escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code), which are short sequences of characters that instruct the terminal to do things such as change the text color, scroll, or other more exotic things.

We only need a few of these escape codes to implement inline apps.

!!! note

    I will gloss over the exact characters used for these escape codes.
    It's enough to know that they exist for now.
    If you implement any of this yourself, refer to the [wikipedia article](https://en.wikipedia.org/wiki/ANSI_escape_code).

## Rendering frames

The first step is to display the app, which is simply text (possibly with escape sequences to change color and style).
The lines are terminated with a newline character (`"\n"`), *except* for the very last line (otherwise we get a blank line a the end which we don't need).
Rather than a final newline, we write an escape code that moves the *cursor* back to it's prior position.

The cursor is where text will be written.
It's the same cursor you see as you type.
Normally it will be at the end of the text in the terminal, but it can be moved around terminal with escape codes.
It can be made invisible (as in Textual apps), but the terminal will keep track of the cursor, even if it can not be seen.

Textual moves the cursor back to its original starting position so that subsequent frames will overwrite the previous frame.

Here's a diagram that shows how the cursor is positioned:

!!! note

    I've drawn the cursor in red, although it isn't typically visible.


<div class="excalidraw">
--8<-- "docs/blog/images/inline1.excalidraw.svg"
</div>


There is an additional consideration that comes in to play when the output has less lines than the previous frame.
If we were to write a shorter frame, it wouldn't fully overwrite the previous frame.
We would be left with a few lines of a previous frame that wouldn't update.

The solution to this problem is to write an escape code that clears lines from the cursor downwards before we write a smaller frame.
You can see this in action in the above video.
The inline app can grow or shrink in size, and still be anchored to the bottom of the terminal.

## Cursor input

The cursor tells the terminal where any text will be written by the app, but it also assumes this will be where the user enters text.
If you enter CJK (Chinese Japanese Korean) text in to the terminal, you will typically see a floating control that points where new text will be written.
If you are on a Mac, the emoji entry dialog (++ctrl+cmd+space++) will also point at the current cursor position. To make this work in a sane way, we need to move the terminal's cursor to where any new text will appear.

The following diagram shows the cursor moving to the point where new text is displayed.

<div class="excalidraw">
--8<-- "docs/blog/images/inline2.excalidraw.svg"
</div>

This only really impacts text entry (such as the [Input](https://textual.textualize.io/widget_gallery/#input) and [TextArea](https://textual.textualize.io/widget_gallery/#textarea) widgets).

## Mouse control

Inline apps in Textual support mouse input, which works the same as fullscreen apps.

To use the mouse in the terminal you send an escape code which tells the terminal to write encoded mouse coordinates to standard input.
The mouse coordinates can then be parsed in much the same was as reading keys.

In inline mode this works in a similar way, with an added complication that the mouse origin is at the top left of the terminal.
In other words if you move the mouse to the top left of the terminal you get coordinate (0, 0), but the app expects (0, 0) to be where it was displayed.

In order for the app to know where the mouse is relative to it's origin, we need to *ask* the terminal where the cursor is.
We do this with an escape code, which tells the terminal to write the current cursor coordinate to standard input.
We can then subtract that coordinate from the physical mouse coordinates, so we can send the app mouse events relative to its on-screen origin.


## tl;dr

[Escapes codes](https://en.wikipedia.org/wiki/ANSI_escape_code).

## Found this interesting?

If you are interested in Textual, join our [Discord server](https://discord.gg/Enf6Z3qhVr).

Or follow me for more terminal shenanigans.

- [@willmcgugan](https://twitter.com/willmcgugan)
- [mastodon.social/@willmcgugan](https://mastodon.social/@willmcgugan)



================================================
FILE: docs/blog/posts/looking-for-help.md
================================================
---
draft: false
date: 2023-01-09
categories:
  - DevLog
authors:
  - davep
---

# So you're looking for a wee bit of Textual help...

## Introduction

!!! quote

    Patience, Highlander. You have done well. But it'll take time. You are
    generations being born and dying. You are at one with all living things.
    Each man's thoughts and dreams are yours to know. You have power beyond
    imagination. Use it well, my friend. Don't lose your head.

    <cite>Juan Sánchez Villalobos Ramírez, Chief metallurgist to King Charles V of Spain</cite>

As of the time of writing, I'm a couple or so days off having been with
Textualize for 3 months. It's been fun, and educational, and every bit as
engaging as I'd hoped, and more. One thing I hadn't quite prepared for
though, but which I really love, is how so many other people are learning
Textual along with me.

<!-- more -->

Even in those three months the library has changed and expanded quite a lot,
and it continues to do so. Meanwhile, more people are turning up and using
the framework; you can see this online in social media, blogs and of course
[in the ever-growing list of projects on GitHub which depend on
Textual](https://github.com/Textualize/textual/network/dependents).

This inevitably means there's a lot of people getting to grips with a new
tool, and one that is still a bit of a moving target. This in turn means
lots of people are coming to us to get help.

As I've watched this happen I've noticed a few patterns emerging. Some of
these good or neutral, some... let's just say not really beneficial to those
seeking the help, or to those trying to provide the help. So I wanted to
write a little bit about the different ways you can get help with Textual
and your Textual-based projects, and to also try and encourage people to
take the most helpful and positive approach to getting that help.

Now, before I go on, I want to make something *very* clear: I'm writing this
as an individual. This is my own personal view, and my own advice from me to
anyone who wishes to take it. It's not Textual (the project) or Textualize
(the company) policy, rules or guidelines. This is just some ageing hacker's
take on how best to go about asking for help, informed by years of asking
for and also providing help in email, on Usenet, on forums, etc.

Or, put another way: if what you read in here seems sensible to you, I
figure we'll likely have already hit it off [over on
GitHub](https://github.com/Textualize/textual) or in [the Discord
server](https://discord.gg/Enf6Z3qhVr). ;-)

## Where to go for help

At this point this is almost a bit of an FAQ itself, so I thought I'd
address it here: where's the best place to ask for help about Textual, and
what's the difference between GitHub Issues, Discussions and our Discord
server?

I'd suggest thinking of them like this:

### Discord

You have a question, or need help with something, and perhaps you could do
with a reply as soon as possible. But, and this is the **really important
part**, it doesn't matter if you don't get a response. If you're in this
situation then the Discord server is possibly a good place to start. If
you're lucky someone will be hanging about who can help out.

I can't speak for anyone else, but keep this in mind: when I look in on
Discord I tend not to go scrolling back much to see if anything has been
missed. If something catches my eye, I'll try and reply, but if it
doesn't... well, it's mostly an instant chat thing so I don't dive too
deeply back in time.

!!! tip inline end "Going from Discord to a GitHub issue"

    As a slight aside here: sometimes people will pop up in Discord, ask a
    question about something that turns out looking like a bug, and that's
    the last we hear of it. Please, please, **please**, if this happens, the
    most helpful thing you can do is go raise an issue for us. It'll help us
    to keep track of problems, it'll help get your problem fixed, it'll mean
    everyone benefits.

My own advice would be to treat Discord as an ephemeral resource. It happens
in the moment but fades away pretty quickly. It's like knocking on a
friend's door to see if they're in. If they're not in, you might leave them
a note, which is sort of like going to...

### GitHub

On the other hand, if you have a question or need some help or something
where you want to stand a good chance of the Textual developers (amongst
others) seeing it and responding, I'd recommend that GitHub is the place to
go. Dropping something into the discussions there, or leaving an issue,
ensures it'll get seen. It won't get lost.

As for which you should use -- a discussion or an issue -- I'd suggest this:
if you need help with something, or you want to check your understanding of
something, or you just want to be sure something is a problem before taking
it further, a discussion might be the best thing. On the other hand, if
you've got a clear bug or feature request on your hands, an issue makes a
lot of sense.

Don't worry if you're not sure which camp your question or whatever falls
into though; go with what you think is right. There's no harm done either
way (I may move an issue to a discussion first before replying, if it's
really just a request for help -- but that's mostly so everyone can benefit
from finding it in the right place later on down the line).

## The dos and don'ts of getting help

Now on to the fun part. This is where I get a bit preachy. Ish. Kinda. A
little bit. Again, please remember, this isn't a set of rules, this isn't a
set of official guidelines, this is just a bunch of *"if you want my advice,
and I know you didn't ask but you've read this far so you actually sort of
did don't say I didn't warn you!"* waffle.

This isn't going to be an exhaustive collection, far from it. But I feel
these are some important highlights.

### Do...

When looking for help, in any of the locations mentioned above, I'd totally
encourage:

#### Be clear and detailed

Too much detail is almost always way better than not enough. *"My program
didn't run"*, often even with some of the code supplied, is so much harder
to help than *"I ran this code I'm posting here, and I expected this
particular outcome, and I expected it because I'd read this particular thing
in the docs and had comprehended it to mean this, but instead the outcome
was this exception here, and I'm a bit stuck -- can someone offer some
pointers?"*

The former approach means there often ends up having to be a back and forth
which can last a long time, and which can sometimes be frustrating for the
person asking. Manage frustration: be clear, tell us everything you can.

#### Say what resources you've used already

If you've read the potions of the documentation that relate to what you're
trying to do, it's going to be really helpful if you say so. If you don't,
it might be assumed you haven't and you may end up being pointed at them.

So, please, if you've checked the documentation, looked in the FAQ, done a
search of past issues or discussions or perhaps even done a search on the
Discord server... please say so.

#### Be polite

This one can go a long way when looking for help. Look, I get it,
programming is bloody frustrating at times. We've all rage-quit some code at
some point, I'm sure. It's likely going to be your moment of greatest
frustration when you go looking for help. But if you turn up looking for
help acting all grumpy and stuff it's not going to come over well. Folk are
less likely to be motivated to lend a hand to someone who seems rather
annoyed.

If you throw in a please and thank-you here and there that makes it all the
better.

#### Fully consider the replies

You could find yourself getting a reply that you're sure won't help at all.
That's fair. But be sure to fully consider it first. Perhaps you missed the
obvious along the way and this is 100% the course correction you'd
unknowingly come looking for in the first place. Sure, the person replying
might have totally misunderstood what was being asked, or might be giving a
wrong answer (it me! I've totally done that and will again!), but even then
a reply along the lines of *"I'm not sure that's what I'm looking for,
because..."* gets everyone to the solution faster than *"lol nah"*.

#### Entertain what might seem like odd questions

Aye, I get it, being asked questions when you're looking for an *answer* can
be a bit frustrating. But if you find yourself on the receiving end of a
small series of questions about your question, keep this in mind: Textual is
still rather new and still developing and it's possible that what you're
trying to do isn't the correct way to do that thing. To the person looking
to help you it may seem to them you have an [XY
problem](https://en.wikipedia.org/wiki/XY_problem).

Entertaining those questions might just get you to the real solution to your
problem.

#### Allow for language differences

You don't need me to tell you that a project such as Textual has a global
audience. With that rather obvious fact comes the other fact that we don't
all share the same first language. So, please, as much as possible, try and
allow for that. If someone is trying to help you out, and they make it clear
they're struggling to follow you, keep this in mind.

#### Acknowledge the answer

I suppose this is a variation on "be polite" (really, a thanks can go a long
way), but there's more to this than a friendly acknowledgement. If someone
has gone to the trouble of offering some help, it's helpful to everyone who
comes after you to acknowledge if it worked or not. That way a future
help-seeker will know if the answer they're reading stands a chance of being
the right one.

#### Accept that Textual is zero-point software (right now)

Of course the aim is to have every release of Textual be stable and useful,
but things will break. So, please, do keep in mind things like:

- Textual likely doesn't have your feature of choice just yet.
- We might accidentally break something (perhaps pinning Textual and testing
  each release is a good plan here?).
- We might deliberately break something because we've decided to take a
  particular feature or way of doing things in a better direction.

Of course it can be a bit frustrating a times, but overall the aim is to
have the best framework possible in the long run.

### Don't...

Okay, now for a bit of old-hacker finger-wagging. Here's a few things I'd
personally discourage:

#### Lack patience

Sure, it can be annoying. You're in your flow, you've got a neat idea for a
thing you want to build, you're stuck on one particular thing and you really
need help right now! Thing is, that's unlikely to happen. Badgering
individuals, or a whole resource, to reply right now, or complaining that
it's been `$TIME_PERIOD` since you asked and nobody has replied... that's
just going to make people less likely to reply.

#### Unnecessarily tag individuals

This one often goes hand in hand with the "lack patience" thing: Be it
asking on Discord, or in GitHub issues, discussions or even PRs,
unnecessarily tagging individuals is a bit rude. Speaking for myself and
only myself: I *love* helping folk with Textual. If I could help everyone
all the time the moment they have a problem, I would. But it doesn't work
like that. There's any number of reasons I might not be responding to a
particular request, including but not limited to (here I'm talking
personally because I don't want to speak for anyone else, but I'm sure I'm
not alone here):

- I have a job. Sure, my job is (in part) Textual, but there's more to it
  than that particular issue. I might be doing other stuff.
- I have my own projects to work on too. I like coding for fun as well (or
  writing preaching old dude blog posts like this I guess, but you get the
  idea).
- I actually have other interests outside of work hours so I might actually
  be out doing a 10k in the local glen, or battling headcrabs in VR, or
  something.
- Housework. :-/

You get the idea though. So while I'm off having a well-rounded life, it's
not good to get unnecessarily intrusive alerts to something that either a)
doesn't actually directly involve me or b) could wait.

#### Seek personal support

Again, I'm going to speak totally for myself here, but I also feel the
general case is polite for all: there's a lot of good support resources
available already; sending DMs on Discord or Twitter or in the Fediverse,
looking for direct personal support, isn't really the best way to get help.
Using the public/collective resources is absolutely the *best* way to get
that help. Why's it a bad idea to dive into DMs? Here's some reasons I think
it's not a good idea:

- It's a variation on "unnecessarily tagging individuals".
- You're short-changing yourself when it comes to getting help. If you ask
  somewhere more public you're asking a much bigger audience, who
  collectively have more time, more knowledge and more experience than a
  single individual.
- Following on from that, any answers can be (politely) fact-checked or
  enhanced by that audience, resulting in a better chance of getting the
  best help possible.
- The next seeker-of-help gets to miss out on your question and the answer.
  If asked and answered in public, it's a record that can help someone else
  in the future.

#### Doubt your ability or skill level

I suppose this should really be phrased as a do rather than a don't, as here
I want to encourage something positive. A few times I've helped people out
who have been very apologetic about their questions being "noob" questions,
or about how they're fairly new to Python, or programming in general.
Really, please, don't feel the need to apologise and don't be ashamed of
where you're at.

If you've asked something that's obviously answered in the documentation,
that's not a problem; you'll likely get pointed at the docs and it's what
happens next that's the key bit. If the attitude is *"oh, cool, that's
exactly what I needed to be reading, thanks!"* that's a really positive
thing. The only time it's a problem is when there's a real reluctance to use
the available resources. We've all seen that person somewhere at some point,
right? ;-)

Not knowing things [is totally cool](https://xkcd.com/1053/).

## Conclusion

So, that's my waffle over. As I said at the start: this is my own personal
thoughts on how to get help with Textual, both as someone whose job it is to
work on Textual and help people with Textual, and also as a FOSS advocate
and supporter who can normally be found helping Textual users when he's not
"on the clock" too.

What I've written here isn't exhaustive. Neither is it novel. Plenty has
been written on the general subject in the past, and I'm sure more will be
written on the subject in the future. I do, however, feel that these are the
most common things I notice. I'd say those dos and don'ts cover 90% of *"can
I get some help?"* interactions; perhaps closer to 99%.

Finally, and I think this is the most important thing to remember, the next
time you are battling some issue while working with Textual: [don't lose
your head](https://www.youtube.com/watch?v=KdYvKF9O7Y8)!



================================================
FILE: docs/blog/posts/on-dog-food-the-original-metaverse-and-not-being-bored.md
================================================
---
draft: false
date: 2022-11-26
categories:
  - DevLog
authors:
  - davep
---

# On dog food, the (original) Metaverse, and (not) being bored

## Introduction

!!! quote

    Cutler, armed with a schedule, was urging the team to "eat its own dog
    food". Part macho stunt and part common sense, the "dog food diet" was the
    cornerstone of Cutler’s philosophy.

    <cite>G. Pascal Zachary &mdash; Show-Stopper!</cite>

I can't remember exactly when it was -- it was likely late in 1994 or some
time in 1995 -- when I first came across the concept of, or rather the name
for the concept of, *"eating your own dog food"*. The idea and the name
played a huge part in the book [*Show-Stopper!* by G. Pascal
Zachary](https://www.gpascalzachary.com/showstopper__the_breakneck_race_to_create_windows_nt_and_the_next_generation_at_m_50101.htm).
The idea wasn't new to me of course; I'd been writing code for over a decade
by then and plenty of times I'd built things and then used those things to
do things, but it was fascinating to a mostly-self-taught 20-something me to
be reading this (excellent -- go read it if you care about the history of
your craft) book and to see the idea written down and named.

<!-- more -->

While [Textualize](https://www.textualize.io/) isn't (thankfully -- really,
I do recommend reading the book) anything like working on the team building
Windows NT, the idea of taking a little time out from working *on* Textual,
and instead work *with* Textual, makes a lot of sense. It's far too easy to
get focused on adding things and improving things and tweaking things while
losing sight of the fact that people will want to build **with** your
product.

So you can imagine how pleased I was when
[Will](https://mastodon.social/@willmcgugan) announced that he wanted [all
of us](https://www.textualize.io/about-us) to spend a couple or so weeks
building something with Textual. I had, of course, already written [one
small application with the
library](https://github.com/Textualize/textual/blob/main/examples/five_by_five.py),
and had plans for another (in part [it's how I ended up working
here](https://blog.davep.org/2022/10/05/on-to-something-new-redux.html)),
but I'd yet to really dive in and try and build something more involved.

Giving it some thought: I wasn't entirely sure what I wanted to build
though. I do want to use Textual to build a brand new terminal-based Norton
Guide reader ([not my first](https://github.com/davep/eg), not by [a long
way](https://github.com/davep/eg-OS2)) but I felt that was possibly a bit
too niche, and actually could take a bit too long anyway. Maybe not, it
remains to be seen.

Eventually I decided on this approach: try and do a quick prototype of some
daft idea each day or each couple of days, do that for a week or so, and
then finally try and settle down on something less trivial. This approach
should work well in that it'll help introduce me to more of Textual, help
try out a few different parts of the library, and also hopefully discover
some real pain-points with working with it and highlight a list of issues we
should address -- as seen from the perspective of a developer working with
the library.

So, here I am, at the end of week one. What I want to try and do is briefly
(yes yes, I know, this introduction is the antithesis of brief) talk about
what I built and perhaps try and highlight some lessons learnt, highlight
some patterns I think are useful, and generally do an end-of-week version of
a [TIL](https://simonwillison.net/2022/Nov/6/what-to-blog-about/). TWIL?

Yeah. I guess this is a TWIL.

## gridinfo

I started the week by digging out a quick hack I'd done a couple of weeks
earlier, with a view to cleaning it up. It started out as a fun attempt to
do something with [Rich Pixels](https://github.com/darrenburns/rich-pixels)
while also making a terminal-based take on
[`slstats.el`](https://github.com/davep/slstats.el). I'm actually pleased
with the result and how quickly it came together.

The point of the application itself is to show some general information
about the current state of the Second Life grid (hello to any fellow
residents of [the original
Metaverse](https://wiki.secondlife.com/wiki/History_of_Second_Life)!), and
to also provide a simple region lookup screen that, using Rich Pixels, will
display the object map (albeit in pretty low resolution -- but that's the
fun of this!).

So the opening screen looks like this:

![The initial screen of gridinfo, showing the main SL stats](../images/2022-11-26-davep-devlog/gridinfo-1.png)

and a lookup of a region looks like this:

![Looking up the details of the first even region](../images/2022-11-26-davep-devlog/gridinfo-2.png)

Here's a wee video of the whole thing in action:

<div class="video-wrapper">
    <iframe
        width="560" height="315"
        src="https://www.youtube.com/embed/dzpGgVPD2aM"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
</div>

### Worth a highlight

Here's a couple of things from the code that I think are worth a highlight,
as things to consider when building Textual apps:

#### Don't use the default screen

Use of the default `Screen` that's provided by the `App` is handy enough,
but I feel any non-trivial application should really put as much code as
possible in screens that relate to key "work". Here's the entirety of my
application code:

```python
class GridInfo( App[ None ] ):
    """TUI app for showing information about the Second Life grid."""

    CSS_PATH = "gridinfo.css"
    """The name of the CSS file for the app."""

    TITLE = "Grid Information"
    """str: The title of the application."""

    SCREENS = {
        "main": Main,
        "region": RegionInfo
    }
    """The collection of application screens."""

    def on_mount( self ) -> None:
        """Set up the application on startup."""
        self.push_screen( "main" )
```

You'll notice there's no work done in the app, other than to declare the
screens, and to set the `main` screen running when the app is mounted.

#### Don't work hard `on_mount`

My initial version of the application had it loading up the data from the
Second Life and GridSurvey APIs in `Main.on_mount`. This obviously wasn't a
great idea as it made the startup appear slow. That's when I realised just
how handy
[`call_after_refresh`](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.call_after_refresh)
is. This meant I could show some placeholder information and then fire off
the requests (3 of them: one to get the main grid information, one to get
the grid concurrency data, and one to get the grid size data), keeping the
application looking active and updating the display when the replies came
in.

### Pain points

While building this app I think there was only really the one pain-point,
and I suspect it's mostly more on me than on Textual itself: getting a good
layout and playing whack-a-mole with CSS. I suspect this is going to be down
to getting more and more familiar with CSS and the terminal (which is
different from laying things out for the web), while also practising with
various layout schemes -- which is where the [revamped `Placeholder`
class](https://textual.textualize.io/blog/2022/11/22/what-i-learned-from-my-first-non-trivial-pr/#what-i-learned-from-my-first-non-trivial-pr)
is going to be really useful.

## unbored

The next application was initially going to be a very quick hack, but
actually turned into a less-trivial build than I'd initially envisaged; not
in a negative way though. The more I played with it the more I explored and
I feel that this ended up being my first really good exploration of some
useful (personal -- your kilometerage may vary) patterns and approaches when
working with Textual.

The application itself is a terminal client for [the
Bored-API](https://www.boredapi.com/). I had initially intended to roll my
own code for working with the API, but I noticed that [someone had done a
nice library for it](https://pypi.org/project/bored-api/) and it seemed
silly to not build on that. Not needing to faff with that, I could
concentrate on the application itself.

At first I was just going to let the user click away at a button that showed
a random activity, but this quickly morphed into a *"why don't I make this
into a sort of TODO list builder app, where you can add things to do when
you are bored, and delete things you don't care for or have done"* approach.

Here's a view of the main screen:

![The main Unbored screen](../images/2022-11-26-davep-devlog/unbored-1.png)

and here's a view of the filter pop-over:

![Setting filters for activities](../images/2022-11-26-davep-devlog/unbored-2.png)

### Worth a highlight

#### Don't put all your `BINDINGS` in one place

This came about from me overloading the use of the `escape` key. I wanted it
to work more or less like this:

- If you're inside an activity, move focus up to the activity type selection
  buttons.
- If the filter pop-over is visible, close that.
- Otherwise exit the application.

It was easy enough to do, and I had an action in the `Main` screen that
`escape` was bound to (again, in the `Main` screen) that did all this logic
with some `if`/`elif` work but it didn't feel elegant. Moreover, it meant
that the `Footer` always displayed the same description for the key.

That's when I realised that it made way more sense to have a `Binding` for
`escape` in every widget that was the actual context for escape's use. So I
went from one top-level binding to...

```python
...

class Activity( Widget ):
    """A widget that holds and displays a suggested activity."""

    BINDINGS = [
        ...
        Binding( "escape", "deselect", "Switch to Types" )
    ]

...

class Filters( Vertical ):
    """Filtering sidebar."""

    BINDINGS = [
        Binding( "escape", "close", "Close Filters" )
    ]

...

class Main( Screen ):
    """The main application screen."""

    BINDINGS = [
        Binding( "escape", "quit", "Close" )
    ]
    """The bindings for the main screen."""
```

This was so much cleaner **and** I got better `Footer` descriptions too. I'm
going to be leaning hard on this approach from now on.

#### Messages are awesome

Until I wrote this application I hadn't really had a need to define or use
my own `Message`s. During work on this I realised how handy they really are.
In the code I have an `Activity` widget which takes care of the job of
moving itself amongst its siblings if the user asks to move an activity up
or down. When this happens I also want the `Main` screen to save the
activities to the filesystem as things have changed.

Thing is: I don't want the screen to know what an `Activity` is capable of
and I don't want an `Activity` to know what the screen is capable of;
especially the latter as I really don't want a child of a screen to know
what the screen can do (in this case *"save stuff"*).

This is where messages come in. Using a message I could just set things up
so that the `Activity` could shout out **"HEY I JUST DID A THING THAT CHANGES
ME"** and not care who is listening and not care what they do with that
information.

So, thanks to this bit of code in my `Activity` widget...

```python
    class Moved( Message ):
        """A message to indicate that an activity has moved."""

    def action_move_up( self ) -> None:
        """Move this activity up one place in the list."""
        if self.parent is not None and not self.is_first:
            parent = cast( Widget, self.parent )
            parent.move_child(
                self, before=parent.children.index( self ) - 1
            )
            self.emit_no_wait( self.Moved( self ) )
            self.scroll_visible( top=True )
```

...the `Main` screen can do this:

```python
    def on_activity_moved( self, _: Activity.Moved ) -> None:
        """React to an activity being moved."""
        self.save_activity_list()
```

!!! warning

    The code above used `emit_no_wait`. Since this blog post was first
    published that method has been removed from Textual. You should use
    [`post_message_no_wait` or `post_message`](/guide/events/#sending-messages) instead now.

### Pain points

On top of the issues of getting to know terminal-based-CSS that I mentioned
earlier:

- Textual currently lacks any sort of selection list or radio-set widget.
  This meant that I couldn't quite do the activity type picking how I would
  have wanted. Of course I could have rolled my own widgets for this, but I
  think I'd sooner wait until such things [are in Textual
  itself](https://textual.textualize.io/roadmap/#widgets).
- Similar to that, I could have used some validating `Input` widgets. They
  too are on the roadmap but I managed to cobble together fairly good
  working versions for my purposes. In doing so though I did further
  highlight that the [reactive attribute
  facility](https://textual.textualize.io/tutorial/#reactive-attributes)
  needs a wee bit more attention as I ran into some
  ([already-known](https://github.com/Textualize/textual/issues/1216)) bugs.
  Thankfully in my case [it was a very easy
  workaround](https://github.com/davep/unbored/blob/d46f7959aeda0996f39d287388c6edd2077be935/unbored#L251-L255).
- Scrolling in general seems a wee bit off when it comes to widgets that are
  more than one line tall. While there's nothing really obvious I can point
  my finger at, I'm finding that scrolling containers sometimes get confused
  about what should be in view. This becomes very obvious when forcing
  things to scroll from code. I feel this deserves a dedicated test
  application to explore this more.

## Conclusion

The first week of *"dogfooding"* has been fun and I'm more convinced than
ever that it's an excellent exercise for Textualize to engage in. I didn't
quite manage my plan of *"one silly trivial prototype per day"*, which means
I've ended up with two (well technically one and a half I guess given that
`gridinfo` already existed as a prototype) applications rather than four.
I'm okay with that. I got a **lot** of utility out of this.

Now to look at the list of ideas I have going and think about what I'll kick
next week off with...



================================================
FILE: docs/blog/posts/placeholder-pr.md
================================================
---
draft: false
date: 2022-11-22
categories:
  - DevLog
authors:
  - rodrigo
---


# What I learned from my first non-trivial PR

<div>
--8<-- "docs/blog/images/placeholder-example.svg"
</div>

It's 8:59 am and, by my Portuguese standards, it is freezing cold outside: 5 or 6 degrees Celsius.
It is my second day at Textualize and I just got into the office.
I undress my many layers of clothing to protect me from the Scottish cold and I sit down in my improvised corner of the Textualize office.
As I sit down, I turn myself in my chair to face my boss and colleagues to ask “So, what should I do today?”.
I was not expecting Will's answer, but the challenge excited me:

<!-- more -->

 > “I thought I'll just throw you in the deep end and have you write some code.”

What happened next was that I spent two days [working on PR #1229](https://github.com/Textualize/textual/pull/1229) to add a new widget to the [Textual](https://github.com/Textualize/textual) code base.
At the time of writing, the pull request has not been merged yet.
Well, to be honest with you, it hasn't even been reviewed by anyone...
But that won't stop me from blogging about some of the things I learned while creating this PR.


## The placeholder widget

This PR adds a widget called `Placeholder` to Textual.
As per the documentation, this widget “is meant to have no complex functionality.
Use the placeholder widget when studying the layout of your app before having to develop your custom widgets.”

The point of the placeholder widget is that you can focus on building the layout of your app without having to have all of your (custom) widgets ready.
The placeholder widget also displays a couple of useful pieces of information to help you work out the layout of your app, namely the ID of the widget itself (or a custom label, if you provide one) and the width and height of the widget.

As an example of usage of the placeholder widget, you can refer to the screenshot at the top of this blog post, which I included below so you don't have to scroll up:

<div>
--8<-- "docs/blog/images/placeholder-example.svg"
</div>

The top left and top right widgets have custom labels.
Immediately under the top right placeholder, you can see some placeholders identified as `#p3`, `#p4`, and `#p5`.
Those are the IDs of the respective placeholders.
Then, rows 2 and 3 contain some placeholders that show their respective size and some placeholders that just contain some text.


## Bootstrapping the code for the widget

So, how does a code monkey start working on a non-trivial PR within 24 hours of joining a company?
The answer is simple: just copy and paste code!
But instead of copying and pasting from Stack Overflow, I decided to copy and paste from the internal code base.

My task was to create a new widget, so I thought it would be a good idea to take a look at the implementation of other Textual widgets.
For some reason I cannot seem to recall, I decided to take a look at the implementation of the button widget that you can find in [_button.py](https://github.com/Textualize/textual/blob/main/src/textual/widgets/_button.py).
By looking at how the button widget is implemented, I could immediately learn a few useful things about what I needed to do and some other things about how Textual works.

For example, a widget can have a class attribute called `DEFAULT_CSS` that specifies the default CSS for that widget.
I learned this just from staring at the code for the button widget.

Studying the code base will also reveal the standards that are in place.
For example, I learned that for a widget with variants (like the button with its “success” and “error” variants), the widget gets a CSS class with the name of the variant prefixed by a dash.
You can learn this by looking at the method `Button.watch_variant`:

```py
class Button(Static, can_focus=True):
    # ...

    def watch_variant(self, old_variant: str, variant: str):
        self.remove_class(f"-{old_variant}")
        self.add_class(f"-{variant}")
```

In short, looking at code and files that are related to the things you need to do is a great way to get information about things you didn't even know you needed.


## Handling the placeholder variant

A button widget can have a different variant, which is mostly used by Textual to determine the CSS that should apply to the given button.
For the placeholder widget, we want the variant to determine what information the placeholder shows.
The [original GitHub issue](https://github.com/Textualize/textual/issues/1200) mentions 5 variants for the placeholder:

 - a variant that just shows a label or the placeholder ID;
 - a variant that shows the size and location of the placeholder;
 - a variant that shows the state of the placeholder (does it have focus? is the mouse over it?);
 - a variant that shows the CSS that is applied to the placeholder itself; and
 - a variant that shows some text inside the placeholder.

The variant can be assigned when the placeholder is first instantiated, for example, `Placeholder("css")` would create a placeholder that shows its own CSS.
However, we also want to have an `on_click` handler that cycles through all the possible variants.
I was getting ready to reinvent the wheel when I remembered that the standard module [`itertools`](https://docs.python.org/3/library/itertools) has a lovely tool that does exactly what I needed!
Thus, all I needed to do was create a new `cycle` through the variants each time a placeholder is created and then grab the next variant whenever the placeholder is clicked:

```py
class Placeholder(Static):
    def __init__(
        self,
        variant: PlaceholderVariant = "default",
        *,
        label: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
    ) -> None:
        # ...

        self.variant = self.validate_variant(variant)
        # Set a cycle through the variants with the correct starting point.
        self._variants_cycle = cycle(_VALID_PLACEHOLDER_VARIANTS_ORDERED)
        while next(self._variants_cycle) != self.variant:
            pass

    def on_click(self) -> None:
        """Click handler to cycle through the placeholder variants."""
        self.cycle_variant()

    def cycle_variant(self) -> None:
        """Get the next variant in the cycle."""
        self.variant = next(self._variants_cycle)
```

I am just happy that I had the insight to add this little `while` loop when a placeholder is instantiated:

```py
from itertools import cycle
# ...
class Placeholder(Static):
    # ...
    def __init__(...):
        # ...
        self._variants_cycle = cycle(_VALID_PLACEHOLDER_VARIANTS_ORDERED)
        while next(self._variants_cycle) != self.variant:
            pass
```

Can you see what would be wrong if this loop wasn't there?


## Updating the render of the placeholder on variant change

If the variant of the placeholder is supposed to determine what information the placeholder shows, then that information must be updated every time the variant of the placeholder changes.
Thankfully, Textual has reactive attributes and watcher methods, so all I needed to do was...
Defer the problem to another method:

```py
class Placeholder(Static):
    # ...
    variant = reactive("default")
    # ...
    def watch_variant(
        self, old_variant: PlaceholderVariant, variant: PlaceholderVariant
    ) -> None:
        self.validate_variant(variant)
        self.remove_class(f"-{old_variant}")
        self.add_class(f"-{variant}")
        self.call_variant_update()  # <-- let this method do the heavy lifting!
```

Doing this properly required some thinking.
Not that the current proposed solution is the best possible, but I did think of worse alternatives while I was thinking how to tackle this.
I wasn't entirely sure how I would manage the variant-dependant rendering because I am not a fan of huge conditional statements that look like switch statements:

```py
if variant == "default":
    # render the default placeholder
elif variant == "size":
    # render the placeholder with its size
elif variant == "state":
    # render the state of the placeholder
elif variant == "css":
    # render the placeholder with its CSS rules
elif variant == "text":
    # render the placeholder with some text inside
```

However, I am a fan of using the built-in `getattr` and I thought of creating a rendering method for each different variant.
Then, all I needed to do was make sure the variant is part of the name of the method so that I can programmatically determine the name of the method that I need to call.
This means that the method `Placeholder.call_variant_update` is just this:

```py
class Placeholder(Static):
    # ...
    def call_variant_update(self) -> None:
        """Calls the appropriate method to update the render of the placeholder."""
        update_variant_method = getattr(self, f"_update_{self.variant}_variant")
        update_variant_method()
```

If `self.variant` is, say, `"size"`, then `update_variant_method` refers to `_update_size_variant`:

```py
class Placeholder(Static):
    # ...
    def _update_size_variant(self) -> None:
        """Update the placeholder with the size of the placeholder."""
        width, height = self.size
        self._placeholder_label.update(f"[b]{width} x {height}[/b]")
```

This variant `"size"` also interacts with resizing events, so we have to watch out for those:

```py
class Placeholder(Static):
    # ...
    def on_resize(self, event: events.Resize) -> None:
        """Update the placeholder "size" variant with the new placeholder size."""
        if self.variant == "size":
            self._update_size_variant()
```


## Deleting code is a (hurtful) blessing

To conclude this blog post, let me muse about the fact that the original issue mentioned five placeholder variants and that my PR only includes two and a half.

After careful consideration and after coming up with the `getattr` mechanism to update the display of the placeholder according to the active variant, I started showing the “final” product to Will and my other colleagues.
Eventually, we ended up getting rid of the variant for CSS and the variant that shows the placeholder state.
This means that I had to **delete part of my code** even before it saw the light of day.

On the one hand, deleting those chunks of code made me a bit sad.
After all, I had spent quite some time thinking about how to best implement that functionality!
But then, it was time to write documentation and tests, and I verified that the **best code** is the code that you don't even write!
The code you don't write is guaranteed to have zero bugs and it also does not need any documentation whatsoever!

So, it was a shame that some lines of code I poured my heart and keyboard into did not get merged into the Textual code base.
On the other hand, I am quite grateful that I won't have to fix the bugs that will certainly reveal themselves in a couple of weeks or months from now.
Heck, the code hasn't been merged yet and just by writing this blog post I noticed a couple of tweaks that were missing!



================================================
FILE: docs/blog/posts/puppies-and-cake.md
================================================
---
draft: false
date: 2023-07-29
categories:
  - DevLog
authors:
  - willmcgugan
title: "Pull Requests are cake or puppies"
---

# Pull Requests are cake or puppies

Broadly speaking, there are two types of contributions you can make to an Open Source project.

<!-- more -->

The first type is typically a bug fix, but could also be a documentation update, linting fix, or other change which doesn't impact core functionality.
Such a contribution is like *cake*.
It's a simple, delicious, gift to the project.

The second type of contribution often comes in the form of a new feature.
This contribution likely represents a greater investment of time and effort than a bug fix.
It is still a gift to the project, but this contribution is *not* cake.

A feature PR has far more in common with a puppy.
The maintainer(s) may really like the feature but hesitate to merge all the same.
They may even reject the contribution entirely.
This is because a feature PR requires an ongoing burden to maintain.
In the same way that a puppy needs food and walkies, a new feature will require updates and fixes long after the original contribution.
Even if it is an amazing feature, the maintainer may not want to commit to that ongoing work.

![Puppy cake](../images/puppy.jpg)

The chances of a feature being merged can depend on the maturity of the project.
At the beginning of a project, a maintainer may be delighted with a new feature contribution.
After all, having others join you to build something is the joy of Open Source.
And yet when a project gets more mature there may be a growing resistance to adding new features, and a greater risk that a feature PR is rejected or sits unappreciated in the PR queue.

So how should a contributor avoid this?
If there is any doubt, it's best to propose the feature to the maintainers before undertaking the work.
In all likelihood they will be happy for your contribution, just be prepared for them to say "thanks but no thanks".
Don't take it as a rejection of your gift: it's just that the maintainer can't commit to taking on a puppy.

There are other ways to contribute code to a project that don't require the code to be merged in to the core.
You could publish your change as a third party library.
Take it from me: maintainers love it when their project spawns an ecosystem.
You could also blog about how you solved your problem without an update to the core project.
Having a resource that can be googled for, or a maintainer can direct people to, can be a huge help.

What prompted me to think about this is that my two main projects, [Rich](https://github.com/Textualize/rich) and [Textual](https://github.com/Textualize/textual), are at quite different stages in their lifetime. Rich is relatively mature, and I'm unlikely to accept a puppy. If you can achieve what you need without adding to the core library, I am *probably* going to decline a new feature. Textual is younger and still accepting puppies &mdash; in addition to stick insects, gerbils, capybaras and giraffes.

!!! tip

    If you are maintainer, and you do have to close a feature PR, feel free to link to this post.

---

Join us on the [Discord Server](https://discord.gg/Enf6Z3qhVr) if you want to discuss puppies and other creatures.



================================================
FILE: docs/blog/posts/release0-11-0.md
================================================
---
draft: false
date: 2023-02-15
categories:
  - Release
title: "Textual 0.11.0 adds a beautiful Markdown widget"
authors:
  - willmcgugan
---

# Textual 0.11.0 adds a beautiful Markdown widget

We released Textual 0.10.0 25 days ago, which is a little longer than our usual release cycle. What have we been up to?

<!-- more -->

The headline feature of this release is the enhanced Markdown support. Here's a screenshot of an example:

<div>
--8<-- "docs/blog/images/markdown-viewer.svg"
</div>

!!! tip

    You can generate these SVG screenshots for your app with `textual run my_app.py --screenshot 5` which will export a screenshot after 5 seconds.

There are actually 2 new widgets: [Markdown](./../../widgets/markdown.md) for a simple Markdown document, and [MarkdownViewer](./../../widgets/markdown_viewer.md) which adds browser-like navigation and a table of contents.

Textual has had support for Markdown since day one by embedding a Rich [Markdown](https://rich.readthedocs.io/en/latest/markdown.html) object -- which still gives decent results! This new widget adds dynamic controls such as scrollable code fences and tables, in addition to working links.

In future releases we plan on adding more Markdown extensions, and the ability to easily embed custom widgets within the document. I'm sure there are plenty of interesting applications that could be powered by dynamically generated Markdown documents.

## DataTable improvements

There has been a lot of work on the [DataTable](../../widgets/data_table.md) API. We've added the ability to sort the data, which required that we introduce the concept of row and column keys. You can now reference rows / columns / cells by their coordinate or by row / column key.

Additionally there are new [update_cell][textual.widgets.DataTable.update_cell] and [update_cell_at][textual.widgets.DataTable.update_cell_at] methods to update cells after the data has been populated. Future releases will have more methods to manipulate table data, which will make it a very general purpose (and powerful) widget.

## Tree control

The [Tree](../../widgets/tree.md) widget has grown a few methods to programmatically expand, collapse and toggle tree nodes.

## Breaking changes

There are a few breaking changes in this release. These are mostly naming and import related, which should be easy to fix if you are affected. Here's a few notable examples:

- `Checkbox` has been renamed to `Switch`. This is because we plan to introduce complimentary `Checkbox` and `RadioButton` widgets in a future release, but we loved the look of *Switches* too much to drop them.
- We've dropped the `emit` and `emit_no_wait` methods. These methods posted message to the parent widget, but we found that made it problematic to subclass widgets. In almost all situations you want to replace these with `self.post_message` (or `self.post_message_no_wait`).

Be sure to check the [CHANGELOG](https://github.com/Textualize/textual/blob/main/CHANGELOG.md) for the full details on potential breaking changes.

## Join us!

We're having fun on our [Discord server](https://discord.gg/Enf6Z3qhVr). Join us there to talk to Textualize developers and share ideas.



================================================
FILE: docs/blog/posts/release0-12-0.md
================================================
---
draft: false
date: 2023-02-24
categories:
  - Release
title: "Textual 0.12.0 adds syntactical sugar and batch updates"
authors:
  - willmcgugan
---

# Textual 0.12.0 adds syntactical sugar and batch updates

It's been just 9 days since the previous release, but we have a few interesting enhancements to the Textual API to talk about.

<!-- more -->

## Better compose

We've added a little *syntactical sugar* to Textual's `compose` methods, which aids both
readability and *editability* (that might not be a word).

First, let's look at the old way of building compose methods. This snippet is taken from the `textual colors` command.


```python
for color_name in ColorSystem.COLOR_NAMES:

    items: list[Widget] = [ColorLabel(f'"{color_name}"')]
    for level in LEVELS:
        color = f"{color_name}-{level}" if level else color_name
        item = ColorItem(
            ColorBar(f"${color}", classes="text label"),
            ColorBar("$text-muted", classes="muted"),
            ColorBar("$text-disabled", classes="disabled"),
            classes=color,
        )
        items.append(item)

    yield ColorGroup(*items, id=f"group-{color_name}")
```

This code *composes* the following color swatches:

<div>
--8<-- "docs/blog/images/colors.svg"
</div>

!!! tip

    You can see this by running `textual colors` from the command line.


The old way was not all that bad, but it did make it hard to see the structure of your app at-a-glance, and editing compose methods always felt a little laborious.

Here's the new syntax, which uses context managers to add children to containers:

```python
for color_name in ColorSystem.COLOR_NAMES:
    with ColorGroup(id=f"group-{color_name}"):
        yield Label(f'"{color_name}"')
        for level in LEVELS:
            color = f"{color_name}-{level}" if level else color_name
            with ColorItem(classes=color):
                yield ColorBar(f"${color}", classes="text label")
                yield ColorBar("$text-muted", classes="muted")
                yield ColorBar("$text-disabled", classes="disabled")
```

The context manager approach generally results in fewer lines of code, and presents attributes on the same line as containers themselves. Additionally, adding widgets to a container can be as simple is indenting them.

You can still construct widgets and containers with positional arguments, but this new syntax is preferred. It's not documented yet, but you can start using it now. We will be updating our examples in the next few weeks.

## Batch updates

Textual is smart about performing updates to the screen. When you make a change that might *repaint* the screen, those changes don't happen immediately. Textual makes a note of them, and repaints the screen a short time later (around a 1/60th of a second). Multiple updates are combined so that Textual does less work overall, and there is none of the flicker you might get with multiple repaints.

Although this works very well, it is possible to introduce a little flicker if you make changes across multiple widgets. And especially if you add or remove many widgets at once. To combat this we have added a [batch_update][textual.app.App.batch_update] context manager which tells Textual to disable screen updates until the end of the with block.

The new [Markdown](./release0-11-0.md) widget uses this context manager when it updates its content. Here's the code:

```python
with self.app.batch_update():
    await self.query("MarkdownBlock").remove()
    await self.mount_all(output)
```

Without the batch update there are a few frames where the old markdown blocks are removed and the new blocks are added (which would be perceived as a brief flicker). With the update, the update appears instant.

## Disabled widgets

A few widgets (such as [Button](./../../widgets/button.md)) had a `disabled` attribute which would fade the widget a little and make it unselectable. We've extended this to all widgets. Although it is particularly applicable to input controls, anything may be disabled. Disabling a container makes its children disabled, so you could use this for disabling a form, for example.

!!! tip

    Disabled widgets may be styled with the `:disabled` CSS pseudo-selector.

## Preventing messages

Also in this release is another context manager, which will disable specified Message types. This doesn't come up as a requirement very often, but it can be very useful when it does. This one is documented, see [Preventing events](./../../guide/events.md#preventing-messages) for details.

## Full changelog

As always see the [release page](https://github.com/Textualize/textual/releases/tag/v0.12.0) for additional changes and bug fixes.

## Join us!

We're having fun on our [Discord server](https://discord.gg/Enf6Z3qhVr). Join us there to talk to Textualize developers and share ideas.



================================================
FILE: docs/blog/posts/release0-14-0.md
================================================
---
draft: false
date: 2023-03-09
categories:
  - Release
title: "Textual 0.14.0 shakes up posting messages"
authors:
  - willmcgugan
---

# Textual 0.14.0 shakes up posting messages

Textual version 0.14.0 has landed just a week after 0.13.0.

!!! note

    We like fast releases for Textual. Fast releases means quicker feedback, which means better code.

What's new?

<!-- more -->

We did a little shake-up of posting [messages](../../guide/events.md) which will simplify building widgets. But this does mean a few breaking changes.

There are two methods in Textual to post messages: `post_message` and `post_message_no_wait`. The former was asynchronous (you needed to `await` it), and the latter was a regular method call. These two methods have been replaced with a single `post_message` method.

To upgrade your project to Textual 0.14.0, you will need to do the following:

- Remove `await` keywords from any calls to `post_message`.
- Replace any calls to `post_message_no_wait` with `post_message`.


Additionally, we've simplified constructing messages classes. Previously all messages required a `sender` argument, which had to be manually set. This was a clear violation of our "no boilerplate" policy, and has been dropped. There is still a `sender` property on messages / events, but it is set automatically.

So prior to 0.14.0 you might have posted messages like the following:

```python
await self.post_message(self.Changed(self, item=self.item))
```

You can now replace it with this simpler function call:

```python
self.post_message(self.Change(item=self.item))
```

This also means that you will need to drop the sender from any custom messages you have created.

If this was code pre-0.14.0:

```python
class MyWidget(Widget):

    class Changed(Message):
        """My widget change event."""
        def __init__(self, sender:MessageTarget, item_index:int) -> None:
            self.item_index = item_index
            super().__init__(sender)

```

You would need to make the following change (dropping `sender`).

```python
class MyWidget(Widget):

    class Changed(Message):
        """My widget change event."""
        def __init__(self, item_index:int) -> None:
            self.item_index = item_index
            super().__init__()

```

If you have any problems upgrading, join our [Discord server](https://discord.gg/Enf6Z3qhVr), we would be happy to help.

See the [release notes](https://github.com/Textualize/textual/releases/tag/v0.14.0) for the full details on this update.



================================================
FILE: docs/blog/posts/release0-15-0.md
================================================
---
draft: false
date: 2023-03-13
categories:
  - Release
title: "Textual 0.15.0 adds a tabs widget"
authors:
  - willmcgugan
---

# Textual 0.15.0 adds a tabs widget

We've just pushed Textual 0.15.0, only 4 days after the previous version. That's a little faster than our typical release cadence of 1 to 2 weeks.

What's new in this release?

<!-- more -->

The highlight of this release is a new [Tabs](./widgets/../../../widgets/tabs.md) widget to display tabs which can be navigated much like tabs in a browser. Here's a screenshot:

<div>
--8<-- "docs/blog/images/tabs_widget.svg"
</div>

In a future release, this will be combined with the [ContentSwitcher](../../widgets/content_switcher.md) widget to create a traditional tabbed dialog. Although Tabs is still useful as a standalone widgets.

!!! tip

    I like to tweet progress with widgets on Twitter. See the [#textualtabs](https://twitter.com/search?q=%23textualtabs&src=typeahead_click) hashtag which documents progress on this widget.

Also in this release is a new [LoadingIndicator](./../../widgets/loading_indicator.md) widget to display a simple animation while waiting for data. Here's a screenshot:

<div>
--8<-- "docs/blog/images/loading_indicator.svg"
</div>

As always, see the [release notes](https://github.com/Textualize/textual/releases/tag/v0.15.0) for the full details on this update.

If you want to talk about these widgets, or anything else Textual related, join us on our [Discord server](https://discord.gg/Enf6Z3qhVr).



================================================
FILE: docs/blog/posts/release0-16-0.md
================================================
---
draft: false
date: 2023-03-22
categories:
  - Release
title: "Textual 0.16.0 adds TabbedContent and border titles"
authors:
  - willmcgugan
---

# Textual 0.16.0 adds TabbedContent and border titles

Textual 0.16.0 lands 9 days after the previous release. We have some new features to show you.

<!-- more -->

There are two highlights in this release. In no particular order, the first is [TabbedContent](../../widgets/tabbed_content.md) which uses a row of *tabs* to navigate content. You will have likely encountered this UI in the desktop and web. I think in Windows they are known as "Tabbed Dialogs".

This widget combines existing [Tabs](../../widgets/tabs.md) and [ContentSwitcher](../../api/content_switcher.md) widgets and adds an expressive interface for composing. Here's a trivial example to use content tabs to navigate a set of three markdown documents:

```python
def compose(self) -> ComposeResult:
    with TabbedContent("Leto", "Jessica", "Paul"):
        yield Markdown(LETO)
        yield Markdown(JESSICA)
        yield Markdown(PAUL)
```

Here's an example of the UI you can create with this widget (note the nesting)!

```{.textual path="docs/examples/widgets/tabbed_content.py" press="j"}
```


## Border titles

The second highlight is a frequently requested feature (FRF?). Widgets now have the two new string properties, `border_title` and `border_subtitle`, which will be displayed within the widget's border.

You can set the alignment of these titles via [`border-title-align`](../../styles/border_title_align.md) and [`border-subtitle-align`](../../styles/border_subtitle_align.md). Titles may contain [Console Markup](https://rich.readthedocs.io/en/latest/markup.html), so you can add additional color and style to the labels.

Here's an example of a widget with a title:

<div>
--8<-- "docs/blog/images/border-title.svg"
</div>

BTW the above is a command you can run to see the various border styles you can apply to widgets.

```
textual borders
```

## Container changes

!!! warning "Breaking change"

    If you have an app that uses any container classes, you should read this section.

We've made a change to containers in this release. Previously all containers had *auto* scrollbars, which means that any container would scroll if its children didn't fit. With nested layouts, it could be tricky to understand exactly which containers were scrolling. In 0.16.0 we split containers in to scrolling and non-scrolling versions. So `Horizontal` will now *not* scroll by default, but `HorizontalScroll` will have automatic scrollbars.


## What else?

As always, see the [release notes](https://github.com/Textualize/textual/releases/tag/v0.16.0) for the full details on this update.

If you want to talk about this update or anything else Textual related, join us on our [Discord server](https://discord.gg/Enf6Z3qhVr).



================================================
FILE: docs/blog/posts/release0-17-0.md
================================================
---
draft: false
date: 2023-03-29
categories:
  - Release
title: "Textual 0.17.0 adds translucent screens and Option List"
authors:
  - willmcgugan
---

# Textual 0.17.0 adds translucent screens and Option List

This is a surprisingly large release, given it has been just 7 days since the last version (and we were down a developer for most of that time).

What's new in this release?

<!-- more -->

There are two new notable features I want to cover. The first is a compositor effect.

## Translucent screens

Textual has a concept of "screens" which you can think of as independent UI modes, each with their own user interface and logic.
The App class keeps a stack of these screens so you can switch to a new screen and later return to the previous screen.

!!! tip inline end "Screens"

    See the [guide](../../guide/screens.md) to learn more about the screens API.

    <a href="/guide/screens">
    <div class="excalidraw">
    --8<-- "docs/images/screens/pop_screen.excalidraw.svg"
    </div>
    </a>

Screens can be used to build modal dialogs by *pushing* a screen with controls / buttons, and *popping* the screen when the user has finished with it.
The problem with this approach is that there was nothing to indicate to the user that the original screen was still there, and could be returned to.

In this release we have added alpha support to the Screen's background color which allows the screen underneath to show through, typically blended with a little color.
Applying this to a screen makes it clear than the user can return to the previous screen when they have finished interacting with the modal.

Here's how you can enable this effect with CSS:

```sass hl_lines="3"
DialogScreen {
    align: center middle;
    background: $primary 30%;
}
```

Setting the background to `$primary` will make the background blue (with the default theme).
The addition of `30%` sets the alpha so that it will be blended with the background.
Here's the kind of effect this creates:

<div>
--8<-- "docs/blog/images/transparent_background.svg"
</div>

There are 4 screens in the above screenshot, one for the base screen and one for each of the three dialogs.
Note how each screen modifies the color of the screen below, but leaves everything visible.

See the [docs on screen opacity](../../guide/screens.md#screen-opacity) if you want to add this to your apps.

## Option list

Textual has had a [ListView](../../widgets/list_view.md) widget for a while, which is an excellent way of navigating a list of items (actually other widgets). In this release we've added an [OptionList](../../widgets/option_list.md) which is similar in appearance, but uses the [line api](../../guide/widgets.md#line-api) under the hood. The Line API makes it more efficient when you approach thousands of items.

```{.textual path="docs/examples/widgets/option_list_strings.py"}
```

The Options List accepts [Rich](https://github.com/Textualize/rich/) *renderable*, which means that anything Rich can render may be displayed in a list. Here's an Option List of tables:

```{.textual path="docs/examples/widgets/option_list_tables.py" columns="100" lines="32"}
```

We plan to build on the `OptionList` widget to implement drop-downs, menus, check lists, etc.
But it is still very useful as it is, and you can add it to apps now.

## What else?

There are a number of fixes regarding refreshing in this release. If you had issues with parts of the screen not updating, the new version should resolve it.

There's also a new logging handler, and a "thick" border type.

See [release notes](https://github.com/Textualize/textual/releases/tag/v0.17.0) for the full details.


## Next week

Next week we plan to take a break from building Textual to *building apps* with Textual.
We do this now and again to give us an opportunity to step back and understand things from the perspective of a developer using Textual.
We will hopefully have something interesting to show from the exercise, and new Open Source apps to share.

## Join us

If you want to talk about this update or anything else Textual related, join us on our [Discord server](https://discord.gg/Enf6Z3qhVr).



================================================
FILE: docs/blog/posts/release0-18-0.md
================================================
---
draft: false
date: 2023-04-04
categories:
  - Release
title: "Textual 0.18.0 adds API for managing concurrent workers"
authors:
  - willmcgugan
---

# Textual 0.18.0 adds API for managing concurrent workers

Less than a week since the last release, and we have a new API to show you.

<!-- more -->

This release adds a new [Worker API](../../guide/workers.md) designed to manage concurrency, both asyncio tasks and threads.

An API to manage concurrency may seem like a strange addition to a library for building user interfaces, but on reflection it makes a lot of sense.
People are building Textual apps to interface with REST APIs, websockets, and processes; and they are running into predictable issues.
These aren't specifically Textual problems, but rather general problems related to async tasks and threads.
It's not enough for us to point users at the asyncio docs, we needed a better answer.

The new `run_worker` method provides an easy way of launching "Workers" (a wrapper over async tasks and threads) which also manages their lifetime.

One of the challenges I've found with tasks and threads is ensuring that they are shut down in an orderly manner. Interestingly enough, Textual already implemented an orderly shutdown procedure to close the tasks that power widgets: children are shut down before parents, all the way up to the App (the root node).
The new API piggybacks on to that existing mechanism to ensure that worker tasks are also shut down in the same order.

!!! tip

    You won't need to worry about this [gnarly issue](https://textual.textualize.io/blog/2023/02/11/the-heisenbug-lurking-in-your-async-code/) with the new Worker API.


I'm particularly pleased with the new `@work` decorator which can turn a coroutine OR a regular function into a Textual Worker object, by scheduling it as either an asyncio task or a thread.
I suspect this will solve 90% of the concurrency issues we see with Textual apps.

See the [Worker API](../../guide/workers.md) for the details.

## Join us

If you want to talk about this update or anything else Textual related, join us on our [Discord server](https://discord.gg/Enf6Z3qhVr).



================================================
FILE: docs/blog/posts/release0-23-0.md
================================================
---
draft: false
date: 2023-05-03
categories:
  - Release
title: "Textual 0.23.0 improves message handling"
authors:
  - willmcgugan
---

# Textual 0.23.0 improves message handling

It's been a busy couple of weeks at Textualize.
We've been building apps with [Textual](https://github.com/Textualize/textual), as part of our *dog-fooding* week.
The first app, [Frogmouth](https://github.com/Textualize/frogmouth), was released at the weekend and already has 1K GitHub stars!
Expect two more such apps this month.

<!-- more -->

<div>
--8<-- "docs/blog/images/frogmouth.svg"
</div>

!!! tip

    Join our [mailing list](http://eepurl.com/hL0BF1) if you would like to be the first to hear about our apps.

We haven't stopped developing Textual in that time.
Today we released version 0.23.0 which has a really interesting API update I'd like to introduce.

Textual *widgets* can send messages to each other.
To respond to those messages, you implement a message handler with a naming convention.
For instance, the [Button](/widget_gallery/#button) widget sends a `Pressed` event.
To handle that event, you implement a method called `on_button_pressed`.

Simple enough, but handler methods are called to handle pressed events from *all* Buttons.
To manage multiple buttons you typically had to write a large `if` statement to wire up each button to the code it should run.
It didn't take many Buttons before the handler became hard to follow.

## On decorator

Version 0.23.0 introduces the [`@on`](/guide/events/#on-decorator) decorator which allows you to dispatch events based on the widget that initiated them.

This is probably best explained in code.
The following two listings respond to buttons being pressed.
The first uses a single message handler, the second uses the decorator approach:

=== "on_decorator01.py"

    ```python title="on_decorator01.py"
    --8<-- "docs/examples/events/on_decorator01.py"
    ```

    1. The message handler is called when any button is pressed

=== "on_decorator02.py"

    ```python title="on_decorator02.py"
    --8<-- "docs/examples/events/on_decorator02.py"
    ```

    1. Matches the button with an id of "bell" (note the `#` to match the id)
    2. Matches the button with class names "toggle" *and* "dark"
    3. Matches the button with an id of "quit"

=== "Output"

    ```{.textual path="docs/examples/events/on_decorator01.py"}
    ```

The decorator dispatches events based on a CSS selector.
This means that you could have a handler per button, or a handler for buttons with a shared class, or parent.

We think this is a very flexible mechanism that will help keep code readable and maintainable.

## Why didn't we do this earlier?

It's a reasonable question to ask: why didn't we implement this in an earlier version?
We were certainly aware there was a deficiency in the API.

The truth is simply that we didn't have an elegant solution in mind until recently.
The `@on` decorator is, I believe, an elegant and powerful mechanism for dispatching handlers.
It might seem obvious in hindsight, but it took many iterations and brainstorming in the office to come up with it!


## Join us

If you want to talk about this update or anything else Textual related, join us on our [Discord server](https://discord.gg/Enf6Z3qhVr).



================================================
FILE: docs/blog/posts/release0-24-0.md
================================================
---
draft: false
date: 2023-05-08
categories:
  - Release
title: "Textual 0.24.0 adds a Select control"
authors:
  - willmcgugan
---

# Textual 0.24.0 adds a Select control

Coming just 5 days after the last release, we have version 0.24.0 which we are crowning the King of Textual releases.
At least until it is deposed by version 0.25.0.

<!-- more -->

The highlight of this release is the new [Select](/widget_gallery/#select) widget: a very familiar control from the web and desktop worlds.
Here's a screenshot and code:

=== "Output (expanded)"

    ```{.textual path="docs/examples/widgets/select_widget.py" press="tab,enter,down,down"}
    ```

=== "select_widget.py"

    ```python
    --8<-- "docs/examples/widgets/select_widget.py"
    ```

=== "select.css"

    ```sass
    --8<-- "docs/examples/widgets/select.css"
    ```

## New styles

This one required new functionality in Textual itself.
The "pull-down" overlay with options presented a difficulty with the previous API.
The overlay needed to appear over any content below it.
This is possible (using [layers](https://textual.textualize.io/styles/layers/)), but there was no simple way of positioning it directly under the parent widget.

We solved this with a new "overlay" concept, which can considered a special layer for user interactions like this Select, but also pop-up menus, tooltips, etc.
Widgets styled to use the overlay appear in their natural place in the "document", but on top of everything else.

A second problem we tackled was ensuring that an overlay widget was never clipped.
This was also solved with a new rule called "constrain".
Applying `constrain` to a widget will keep the widget within the bounds of the screen.
In the case of `Select`, if you expand the options while at the bottom of the screen, then the overlay will be moved up so that you can see all the options.

These new rules are currently undocumented as they are still subject to change, but you can see them in the [Select](https://github.com/Textualize/textual/blob/main/src/textual/widgets/_select.py#L179) source if you are interested.

In a future release these will be finalized and you can confidently use them in your own projects.

## Fixes for the @on decorator

The new `@on` decorator is proving popular.
To recap, it is a more declarative and finely grained way of dispatching messages.
Here's a snippet from the [calculator](https://github.com/Textualize/textual/blob/main/examples/calculator.py) example which uses `@on`:

```python
    @on(Button.Pressed, "#plus,#minus,#divide,#multiply")
    def pressed_op(self, event: Button.Pressed) -> None:
        """Pressed one of the arithmetic operations."""
        self.right = Decimal(self.value or "0")
        self._do_math()
        assert event.button.id is not None
        self.operator = event.button.id
```

The decorator arranges for the method to be called when any of the four math operation buttons are pressed.

In 0.24.0 we've fixed some missing attributes which prevented the decorator from working with some messages.
We've also extended the decorator to use keywords arguments, so it will match attributes other than `control`.

## Other fixes

There is a surprising number of fixes in this release for just 5 days. See [CHANGELOG.md](https://github.com/Textualize/textual/blob/main/CHANGELOG.md) for details.


## Join us

If you want to talk about this update or anything else Textual related, join us on our [Discord server](https://discord.gg/Enf6Z3qhVr).



================================================
FILE: docs/blog/posts/release0-27-0.md
================================================
---
draft: false
date: 2023-06-01
categories:
  - Release
title: "Textual adds Sparklines, Selection list, Input validation, and tool tips"
authors:
  - willmcgugan
---

# Textual adds Sparklines, Selection list, Input validation, and tool tips

It's been 12 days since the last Textual release, which is longer than our usual release cycle of a week.

We've been a little distracted with our "dogfood" projects: [Frogmouth](https://github.com/Textualize/frogmouth) and [Trogon](https://github.com/Textualize/trogon). Both of which hit 1000 Github stars in 24 hours. We will be maintaining / updating those, but it is business as usual for this Textual release (and it's a big one). We have such sights to show you.

<!-- more -->

## Sparkline widget

A [Sparkline](../../widget_gallery.md#sparkline) is essentially a mini-plot. Just detailed enough to keep an eye on time-series data.

<div>
--8<-- "docs/blog/images/sparkline.svg"
</div>

Colors are configurable, and all it takes is a call to [`set_interval`](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_interval) to make it animate.

## Selection list

Next up is the [SelectionList](../../widget_gallery.md#selectionlist) widget. Essentially a scrolling list of checkboxes. Lots of use cases for this one.

<div>
--8<-- "docs/blog/images/selection-list.svg"
</div>

## Tooltips

We've added [tooltips](../../guide/widgets.md#tooltips) to Textual widgets.

The API couldn't be simpler: simply assign a string to the `tooltip` property on any widget.
This string will be displayed after 300ms when you hover over the widget.


<div>
--8<-- "docs/blog/images/tooltips.svg"
</div>

As always, you can configure how the tooltips will be displayed with CSS.

## Input updates

We have some quality of life improvements for the [Input](../../widget_gallery.md#input) widget.

You can now use a simple declarative API to [validating input](/widgets/input/#validating-input).

<div>
--8<-- "docs/blog/images/validation.svg"
</div>

Also in this release is a suggestion API, which will *suggest* auto completions as you type.
Hit <kbd>right</kbd> to accept the suggestion.

Here's a screenshot:

<div>
--8<-- "docs/blog/images/suggest.svg"
</div>

You could use this API to offer suggestions from a fixed list, or even pull the data from a network request.

## Join us

Development on Textual is *fast*.
We're very responsive to issues and feature requests.

If you have any suggestions, jump on our [Discord server](https://discord.gg/Enf6Z3qhVr) and you may see your feature in the next release!



================================================
FILE: docs/blog/posts/release0-29-0.md
================================================
---
draft: false
date: 2023-07-03
categories:
  - Release
title: "Textual 0.29.0 refactors dev tools"
authors:
  - willmcgugan
---

# Textual 0.29.0 refactors dev tools

It's been a slow week or two at Textualize, with Textual devs taking well-earned annual leave, but we still managed to get a new version out.

<!-- more -->

Version 0.29.0 has shipped with a number of fixes (see the [release notes](https://github.com/Textualize/textual/releases/tag/v0.29.0) for details), but I'd like to use this post to explain a change we made to how Textual developer tools are distributed.

Previously if you installed `textual[dev]` you would get the Textual dev tools plus the library itself. If you were distributing Textual apps and didn't need the developer tools you could drop the `[dev]`.

We did this because the less dependencies a package has, the fewer installation issues you can expect to get in the future. And Textual is surprisingly lean if you only need to *run* apps, and not build them.

Alas, this wasn't quite as elegant solution as we hoped. The dependencies defined in extras wouldn't install commands, so `textual` was bundled with the core library. This meant that if you installed the Textual package *without* the `[dev]` you would still get the `textual` command on your path but it wouldn't run.

We solved this by creating two packages: `textual` contains the core library (with minimal dependencies) and `textual-dev` contains the developer tools. If you are building Textual apps, you should install both as follows:

```
pip install textual textual-dev
```

That's the only difference. If you run in to any issues feel free to ask on the [Discord server](https://discord.gg/Enf6Z3qhVr)!



================================================
FILE: docs/blog/posts/release0-30-0.md
================================================
---
draft: false
date: 2023-07-17
categories:
  - Release
title: "Textual 0.30.0 adds desktop-style notifications"
authors:
  - willmcgugan
---

# Textual 0.30.0 adds desktop-style notifications

We have a new release of Textual to talk about, but before that I'd like to cover a little Textual news.

<!-- more -->

By sheer coincidence we reached [20,000 stars on GitHub](https://github.com/Textualize/textual) today.
Now stars don't mean all that much (at least until we can spend them on coffee), but its nice to know that twenty thousand developers thought Textual was interesting enough to hit the ★ button.
Thank you!

In other news: we moved office.
We are now a stone's throw away from Edinburgh Castle.
The office is around three times as big as the old place, which means we have room for wide standup desks and dual monitors.
But more importantly we have room for new employees.
Don't send your CVs just yet, but we hope to grow the team before the end of the year.

Exciting times.

## New Release

And now, for the main feature.
Version 0.30 adds a new notification system.
Similar to desktop notifications, it displays a small window with a title and message (called a *toast*) for a pre-defined number of seconds.

Notifications are great for short timely messages to add supplementary information for the user.
Here it is in action:

<div class="video-wrapper">
    <iframe
        width="560" height="315"
        src="https://www.youtube.com/embed/HIHRefjfcVc"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
</div>

The API is super simple.
To display a notification, call `notify()` with a message and an optional title.

```python
def on_mount(self) -> None:
    self.notify("Hello, from Textual!", title="Welcome")
```

## Textualize Video Channel

In case you missed it; Textualize now has a [YouTube](https://www.youtube.com/channel/UCo4nHAZv_cIlAiCSP2IyiOA) channel.
Our very own [Rodrigo](https://twitter.com/mathsppblog) has recorded a video tutorial series on how to build Textual apps.
Check it out!

<div class="video-wrapper">
    <iframe
        width="560" height="315"
        src="https://www.youtube.com/embed/kpOBRI56GXM"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
</div>

We will be adding more videos in the near future, covering anything from beginner to advanced topics.

Don't worry if you prefer reading to watching videos.
We will be adding plenty more content to the [Textual docs](https://textual.textualize.io/) in the near future.
Watch this space.

As always, if you want to discuss anything with the Textual developers, join us on the [Discord server](https://discord.gg/Enf6Z3qhVr).



================================================
FILE: docs/blog/posts/release0-38-0.md
================================================
---
draft: false
date: 2023-09-21
categories:
  - Release
title: "Textual 0.38.0 adds a syntax aware TextArea"
authors:
  - willmcgugan
---

# Textual 0.38.0 adds a syntax aware TextArea

This is the second big feature release this month after last week's [command palette](./release0.37.0.md).

<!-- more -->

The [TextArea](../../widgets/text_area.md) has finally landed.
I know a lot of folk have been waiting for this one.
Textual's TextArea is a fully-featured widget for editing code, with syntax highlighting and line numbers.
It is highly configurable, and looks great.

Darren Burns (the author of this widget) has penned a terrific write-up on the TextArea.
See [Things I learned while building Textual's TextArea](./text-area-learnings.md) for some of the challenges he faced.


## Scoped CSS

Another notable feature added in 0.38.0 is *scoped* CSS.
A common gotcha in building Textual widgets is that you could write CSS that impacted styles outside of that widget.

Consider the following widget:

```python
class MyWidget(Widget):
    DEFAULT_CSS = """
    MyWidget {
        height: auto;
        border: magenta;
    }
    Label {
        border: solid green;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("foo")
        yield Label("bar")
```

The author has intended to style the labels in that widget by adding a green border.
This does work for the widget in question, but (prior to 0.38.0) the `Label` rule would style *all* Labels (including any outside of the widget) &mdash; which was probably not intended.

With version 0.38.0, the CSS is scoped so that only the widget's labels will be styled.
This is almost always what you want, which is why it is enabled by default.
If you do want to style something outside of the widget you can set `SCOPED_CSS=False` (as a classvar).


## Light and Dark pseudo selectors

We've also made a slight quality of life improvement to the CSS, by adding `:light` and `:dark` pseudo selectors.
This allows you to change styles depending on whether the app is currently using a light or dark theme.

This was possible before, just a little verbose.
Here's how you would do it in 0.37.0:

```css
App.-dark-mode MyWidget Label {
    ...
}
```

In 0.38.0 it's a little more concise and readable:

```css
MyWidget:dark Label {
    ...
}
```

## Testing guide

Not strictly part of the release, but we've added a [guide on testing](/guide/testing) Textual apps.

As you may know, we are on a mission to make TUIs a serious proposition for critical apps, which makes testing essential.
We've extracted and documented our internal testing tools, including our snapshot tests pytest plugin [pytest-textual-snapshot](https://pypi.org/project/pytest-textual-snapshot/).

This gives devs powerful tools to ensure the quality of their apps.
Let us know your thoughts on that!

## Release notes

See the [release](https://github.com/Textualize/textual/releases/tag/v0.38.0) page for the full details on this release.


## What's next?

There's lots of features planned over the next few months.
One feature I am particularly excited by is a widget to generate plots by wrapping the awesome [Plotext](https://pypi.org/project/plotext/) library.
Check out some early work on this feature:

<div class="video-wrapper">
<iframe width="1163" height="1005" src="https://www.youtube.com/embed/A3uKzWErC8o" title="Preview of Textual Plot widget" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

## Join us

Join our [Discord server](https://discord.gg/Enf6Z3qhVr) if you want to discuss Textual with the Textualize devs, or the community.



================================================
FILE: docs/blog/posts/release0-4-0.md
================================================
---
draft: false
date: 2022-11-08
categories:
  - Release
authors:
  - willmcgugan
---

# Version 0.4.0

We've released version 0.4.0 of [Textual](https://pypi.org/search/?q=textual).

As this is the first post tagged with `release` let me first explain where the blog fits in with releases. We plan on doing a post for every note-worthy release. Which likely means all but the most trivial updates (typos just aren't that interesting). Blog posts will be supplementary to release notes which you will find on the [Textual repository](https://github.com/Textualize/textual).

Blog posts will give a little more background for the highlights in a release, and a rationale for changes and new additions. We embrace *building in public*, which means that we would like you to be as up-to-date with new developments as if you were sitting in our office. It's a small office, and you might not be a fan of the Scottish weather (it's [dreich](https://www.bbc.co.uk/news/uk-scotland-50476008)), but you can at least be here virtually.

<!-- more -->

Release 0.4.0 follows 0.3.0, released on October 31st. Here are the highlights of the update.

## Updated Mount Method

The [mount](/api/widget/#textual.widget.Widget.mount) method has seen some work. We've dropped the ability to assign an `id` via keyword attributes, which wasn't terribly useful. Now, an `id` must be assigned via the constructor.

The mount method has also grown `before` and `after` parameters which tell Textual where to add a new Widget (the default was to add it to the end). Here are a few examples:

```python

# Mount at the start
self.mount(Button(id="Buy Coffee"), before=0)

# Mount after a selector
self.mount(Static("Password is incorrect"), after="Dialog Input.-error")

# Mount after a specific widget
tweet = self.query_one("Tweet")
self.mount(Static("Consider switching to Mastodon"), after=tweet)

```

Textual needs much of the same kind of operations as the [JS API](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild) exposed by the browser. But we are determined to make this way more intuitive. The new mount method is a step towards that.

## Faster Updates

Textual now writes to stdout in a thread. The upshot of this is that Textual can work on the next update before the terminal has displayed the previous frame.

This means smoother updates all round! You may notice this when scrolling and animating, but even if you don't, you will have more CPU cycles to play with in your Textual app.

<div class="excalidraw">
--8<-- "docs/blog/images/faster-updates.excalidraw.svg"
</div>


## Multiple CSS Paths

Up to version 0.3.0, Textual would only read a single CSS file set in the `CSS_PATH` class variable. You can now supply a list of paths if you have more than one CSS file.

This change was prompted by [tuilwindcss](https://github.com/koaning/tuilwindcss/) which brings a TailwindCSS like approach to building Textual Widgets. Also check out [calmcode.io](https://calmcode.io/) by the same author, which is an amazing resource.



================================================
FILE: docs/blog/posts/release0-6-0.md
================================================
---
draft: false
date: 2022-12-11
categories:
  - Release
title: "version-060"
authors:
  - willmcgugan
---

# Textual 0.6.0 adds a *tree*mendous new widget

A new release of Textual lands 3 weeks after the previous release -- and it's a big one.

<!-- more -->

!!! information

    If you're new here, [Textual](https://github.com/Textualize/textual) is TUI framework for Python.

## Tree Control

The headline feature of version 0.6.0 is a new tree control built from the ground-up. The previous Tree control suffered from an overly complex API and wasn't scalable (scrolling slowed down with 1000s of nodes).

This new version has a simpler API and is highly scalable (no slowdown with larger trees). There are also a number of visual enhancements in this version.

Here's a very simple example:

=== "Output"

    ```{.textual path="docs/examples/widgets/tree.py"}
    ```

=== "tree.py"

    ```python
    --8<-- "docs/examples/widgets/tree.py"
    ```

Here's the tree control being used to navigate some JSON ([json_tree.py](https://github.com/Textualize/textual/blob/main/examples/json_tree.py) in the examples directory).

<div class="video-wrapper">
<iframe width="auto"  src="https://www.youtube.com/embed/Fy9fPL37P6o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

I'm biased of course, but I think this terminal based tree control is more usable (and even prettier) than just about anything I've seen on the web or desktop. So much of computing tends to organize itself in to a tree that I think this widget will find a lot of uses.

The Tree control forms the foundation of the [DirectoryTree](../../widgets/directory_tree.md) widget, which has also been updated. Here it is used in the [code_browser.py](https://github.com/Textualize/textual/blob/main/examples/code_browser.py) example:

<div class="video-wrapper">
<iframe width="auto" src="https://www.youtube.com/embed/ZrYWyZXuYRY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## List View

We have a new [ListView](../../widgets/list_view.md) control to navigate and select items in a list. Items can be widgets themselves, which makes this a great platform for building more sophisticated controls.

=== "Output"

    ```{.textual path="docs/examples/widgets/list_view.py"}
    ```

=== "list_view.py"

    ```python
    --8<-- "docs/examples/widgets/list_view.py"
    ```

=== "list_view.css"

    ```sass
    --8<-- "docs/examples/widgets/list_view.css"
    ```

## Placeholder

The [Placeholder](../../widgets/placeholder.md) widget was broken since the big CSS update. We've brought it back and given it a bit of a polish.

Use this widget in place of custom widgets you have yet to build when designing your UI. The colors are automatically cycled to differentiate one placeholder from the next. You can click a placeholder to cycle between its ID, size, and lorem ipsum text.

=== "Output"

    ```{.textual path="docs/examples/widgets/placeholder.py" columns="100" lines="45"}
    ```

=== "placeholder.py"

    ```python
    --8<-- "docs/examples/widgets/placeholder.py"
    ```

=== "placeholder.css"

    ```sass
    --8<-- "docs/examples/widgets/placeholder.css"
    ```


## Fixes

As always, there are a number of fixes in this release. Mostly related to layout. See [CHANGELOG.md](https://github.com/Textualize/textual/blob/main/CHANGELOG.md) for the details.

## What's next?

The next release will focus on *pain points* we discovered while in a dog-fooding phase (see the [DevLog](https://textual.textualize.io/blog/category/devlog/) for details on what Textual devs have been building).




================================================
FILE: docs/blog/posts/release0.37.0.md
================================================
---
draft: false
date: 2023-09-15
categories:
  - Release
title: "Textual 0.37.0 adds a command palette"
authors:
  - willmcgugan
---


# Textual 0.37.0 adds a command palette

Textual version 0.37.0 has landed!
The highlight of this release is the new command palette.

<!-- more -->

A command palette gives users quick access to features in your app.
If you hit ctrl+backslash in a Textual app, it will bring up the command palette where you can start typing commands.
The commands are matched with a *fuzzy* search, so you only need to type two or three characters to get to any command.

Here's a video of it in action:

<div class="video-wrapper">
<iframe width="1280" height="auto" src="https://www.youtube.com/embed/sOMIkjmM4MY" title="" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Adding your own commands to the command palette is a piece of cake.
Here's the (command) Provider class used in the example above:

```python
class ColorCommands(Provider):
    """A command provider to select colors."""

    async def search(self, query: str) -> Hits:
        """Called for each key."""
        matcher = self.matcher(query)
        for color in COLOR_NAME_TO_RGB.keys():
            score = matcher.match(color)
            if score > 0:
                yield Hit(
                    score,
                    matcher.highlight(color),
                    partial(self.app.post_message, SwitchColor(color)),
                )
```

And here is how you add a provider to your app:

```python
class ColorApp(App):
    """Experiment with the command palette."""

    COMMANDS = App.COMMANDS | {ColorCommands}
```

We're excited about this feature because it is a step towards bringing a common user interface to Textual apps.

!!! quote

    It's a Textual app. I know this.

    &mdash; You, maybe.

The goal is to be able to build apps that may look quite different, but take no time to learn, because once you learn how to use one Textual app, you can use them all.

See the Guide for details on how to work with the [command palette](../../guide/command_palette.md).

## What else?

Also in 0.37.0 we have a new [Collapsible](/widget_gallery/#collapsible) widget, which is a great way of adding content while avoiding a cluttered screen.

And of course, bug fixes and other updates. See the [release](https://github.com/Textualize/textual/releases/tag/v0.37.0) page for the full details.

## What's next?

Coming very soon, is a new TextEditor widget.
This is a super powerful widget to enter arbitrary text, with beautiful syntax highlighting for a number of languages.
We're expecting that to land next week.
Watch this space, or join the [Discord server](https://discord.gg/Enf6Z3qhVr) if you want to be the first to try it out.

## Join us

Join our [Discord server](https://discord.gg/Enf6Z3qhVr) if you want to discuss Textual with the Textualize devs, or the community.



================================================
FILE: docs/blog/posts/release1.0.0.md
================================================
---
draft: false
date: 2024-12-12
categories:
  - Release
title: "Algorithms for high performance terminal apps"
authors:
  - willmcgugan
---


I've had the fortune of being able to work fulltime on a FOSS project for the last three plus years.


<div style="width:250px;float:right;margin:10px;max-width:50%;">
<a href="https://github.com/textualize/textual-demo">
--8<-- "docs/blog/images/textual-demo.svg"
</a>
</div>


Textual has been a constant source of programming challenges.
Often frustrating but never boring, the challenges arise because the terminal "specification" says nothing about how to build a modern User Interface.
The building blocks are there: after some effort you can move the cursor, write colored text, read keys and mouse movements, but that's about it.
Everything else we had to build from scratch. From the most basic [button](https://textual.textualize.io/widget_gallery/#button) to a syntax highlighted [TextArea](https://textual.textualize.io/widget_gallery/#textarea), and everything along the way.

I wanted to write-up some of the solutions we came up with, and the 1.0 milestone we just passed makes this a perfect time.

<!-- more -->

Run the demo with a single line (with [uv](https://docs.astral.sh/uv/) is installed):

```
uvx --python 3.12 textual-demo
```



## The Compositor

The first component of Textual I want to cover is the [compositor](https://github.com/Textualize/textual/blob/main/src/textual/_compositor.py).
The job of the compositor is to combine content from multiple sources into a single view.

We do this because the terminal itself has no notion of overlapping windows in the way a desktop does.

Here's a video I generated over a year ago, demonstrating the compositor:

<div class="video-wrapper">
<iframe width="100%" height="auto" src="https://www.youtube.com/embed/T8PZjUVVb50" title="" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

### The algorithm

You could be forgiven in thinking that the terminal is regular grid of characters and we can treat it like a 2D array.
If that were the case, we could use [painter's algorithm](https://en.wikipedia.org/wiki/Painter's_algorithm) to handle the overlapping widgets.
In other words, sort them back to front and render them as though they were bitmaps.

Unfortunately the terminal is *not* a true grid.
Some characters such as those in Asian languages and many emoji are double the width of latin alphabet characters &mdash; which complicates things (to put it mildly).

Textual's way of handling this is inherited from [Rich](https://github.com/Textualize/rich).
Anything you print in Rich, first generates a list of [Segments](https://github.com/Textualize/rich/blob/master/rich/segment.py) which consist of a string and associated style.
These Segments are converted into text with [ansi escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code) at the very end of the process.


The compositor takes lists of segments generated by widgets and further processes them, by dividing and combining, to produce the final output.
In fact almost everything Textual does involves processing these segments in one way or another.

!!! tip "Switch the Primitive"

    If a problem is intractable, it can often be simplified by changing what you consider to be the atomic data and operations you are working with.
    I call this "switching the primitive".
    In Rich this was switching from thinking in characters to thinking in segments.

### Thinking in Segments

In the following illustration we have an app with three widgets; the background "screen" (in blue) plus two floating widgets (in red and green).
There will be many more widgets in a typical app, but this is enough to show how it works.


<div class="excalidraw">
--8<-- "docs/blog/images/compositor/widgets.excalidraw.svg"
</div>

The lines are lists of Segments produced by the widget renderer.
The compositor will combine those lists in to a single list where nothing overlaps.

To illustrate how this process works, let's consider the highlighted line about a quarter of the way down.


### Compositing a line

Imagine you could view the terminal and widgets side on, so that you see a cross section of the terminal and the floating widgets.
It would appear something like the following:

<div class="excalidraw">
--8<-- "docs/blog/images/compositor/cuts0.excalidraw.svg"
</div>

We can't yet display the output as it would require writing each "layer" independently, potentially making the terminal flicker, and certainly writing more data than necessary.

We need a few more steps to combine these lines in to a single line.


### Step 1. Finding the cuts.

First thing the compositor does is to find every offset where a list of segments begins or ends.
We call these "cuts".

<div class="excalidraw">
--8<-- "docs/blog/images/compositor/cuts1.excalidraw.svg"
</div>

### Step 2. Applying the cuts.

The next step is to divide every list of segments at the cut offsets.
This will produce smaller lists of segments, which we refer to as *chops*.

<div class="excalidraw">
--8<-- "docs/blog/images/compositor/cuts2.excalidraw.svg"
</div>

After this step we have lists of chops where each chop is of the same size, and therefore nothing overlaps.
It's the non-overlapping property that makes the next step possible.

### Step 3. Discard chops.

Only the top-most chops will actually be visible to the viewer.
Anything not at the top will be occluded and can be thrown away.

<div class="excalidraw">
--8<-- "docs/blog/images/compositor/cuts3.excalidraw.svg"
</div>

### Step 4. Combine.

Now all that's left is to combine the top-most chops in to a single list of Segments.
It is this list of segments that becomes a line in the terminal.

<div class="excalidraw">
--8<-- "docs/blog/images/compositor/cuts4.excalidraw.svg"
</div>

As this is the final step in the process, these lines of segments will ultimately be converted to text plus escape sequences and written to the output.

### What I omitted

There is more going on than this explanation may suggest.
Widgets may contain other widgets which are clipped to their *parent's* boundaries, and widgets that contain other widgets may also scroll &mdash; the compositor must take all of this in to account.

!!! info "It's widgets all the way down"

    Not to mention there can be multiple "screens" of widgets stacked on top of each other, with a modal fade effect applied to lower screens.

The compositor can also do partial updates.
In other words, if you click a button and it changes color, the compositor can update just the region occupied by the button.

The compositor does all of this fast enough to enable smooth scrolling, even with a metric tonne of widgets on screen.

## Spatial map

Textual apps typically contain many widgets of different sizes and at different locations within the terminal.
Not all of which widgets may be visible in the final view (if they are within a scrolling container).


!!! info "The smallest Widget"

    While it is possible to have a widget as small as a single character, I've never found a need for one.
    The closest we get in Textual is a [scrollbar corner](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBarCorner);
    a widget which exists to fill the space made when a vertical scrollbar and a horizontal scrollbar meet.
    It does nothing because it doesn't need to, but it is powered by an async task like all widgets and can receive input.
    I have often wondered if there could be something useful in there.
    A game perhaps?
    If you can think of a game that can be played in 2 characters &mdash; let me know!

The *spatial map*[^1] is a data structure used by the compositor to very quickly discard widgets that are not visible within a given region.
The algorithm it uses may be familiar if you have done any classic game-dev.


### The problem

Consider the following arrangement of widgets:

<div class="excalidraw">
--8<-- "docs/blog/images/compositor/spatial-map.excalidraw.svg"
</div>

Here we have 8 widgets, where only 3 or 4 will be visible at any given time, depending on the position of the scrollbar.
We want to avoid doing work on widgets which will not be seen in the next frame.

A naive solution to this would be to check each widget's [Region][textual.geometry.Region] to see if it overlaps with the visible area.
This is a perfectly reasonable solution, but it won't scale well.
If we get in to the 1000s of widgets territory, it may become significant &mdash; and we may have to do this 30 times a second if we are scrolling.

### The Grid

The first step in the spatial map is to associate every widget with a tile in a regular grid[^2].

<div class="excalidraw">
--8<-- "docs/blog/images/compositor/spatial-map-grid.excalidraw.svg"
</div>

The size of the grid is fairly arbitrary, but it should be large enough to cover the viewable area with a relatively small number of grid tiles.
We use a grid size of 100 characters by 20 lines, which seems about right.

When the spatial map is first created it places each widget in one or more grid tiles.
At the end of that process we have a dict that maps every grid coordinate on to a list of widgets, which will look something like the following:

```python
{
    (0, 0): [widget1, widget2, widget3],
    (1, 0): [widget1, widget2, widget3],
    (0, 1): [widget4, widget5, widget6],
    (1, 1): [widget4, widget5, widget6],
    (0, 2): [widget7, widget8],
    (1, 2): [Widget7, widget8]
}
```

The up-front cost of [calculating](https://github.com/Textualize/textual/blob/main/src/textual/_spatial_map.py) this data is fairly low.
It is also very cacheable &mdash; we *do not* need to recalculate it when the user is just scrolling.

### Search the grid

The speedups from the spatial map come when we want to know which widgets are visible.
To do that, we first create a region that covers the area we want to consider &mdash; which may be the entire screen, or a smaller scrollable container.

In the following illustration we have scrolled the screen up[^3] a little so that Widget 3 is at the top of the screen:

<div class="excalidraw">
--8<-- "docs/blog/images/compositor/spatial-map-view1.excalidraw.svg"
</div>

We then determine which grid tiles overlap the viewable area.
In the above examples that would be the tiles with coordinates  `(0,0)`, `(1,0)`, `(0,1)`, and `(1,1)`.
Once we have that information, we can then then look up those coordinates in the spatial map data structure, which would retrieve 4 lists:

```python
[
  [widget1, widget2, widget3],
  [widget1, widget2, widget3],
  [widget4, widget5, widget6],
  [widget4, widget5, widget6],
]
```

Combining those together and de-duplicating we get:

```python
[widget1, widget2, widget3, widget4, widget5, widget6]
```

These widgets are either within the viewable area, or close by.
We can confidently conclude that the widgets *not* ion that list are hidden from view.
If we need to know precisely which widgets are visible we can check their regions individually.

The useful property of this algorithm is that as the number of widgets increases, the time it takes to figure out which are visible stays relatively constant. Scrolling a view of 8 widgets, takes much the same time as a view of 1000 widgets or more.

The code for our `SpatialMap` isn't part of the public API and therefore not in the docs, but if you are interested you can check it out here: [_spatial_map.py](https://github.com/Textualize/textual/blob/main/src/textual/_spatial_map.py).

## Wrapping up

If any of the code discussed here interests you, you have my blessing to [steal the code](./steal-this-code.md)!

As always, if you want to discuss this or Textual in general, we can be found on our [Discord server](https://discord.gg/Enf6Z3qhVr).



[^1]: A term I coined for the structure in Textual. There may be other unconnected things known as spatial maps.
[^2]: The [grid](https://www.youtube.com/watch?v=lILHEnz8fTk&ab_channel=DaftPunk-Topic).
[^3]: If you scroll the screen up, it moves *down* relative to the widgets.



================================================
FILE: docs/blog/posts/remote-memray.md
================================================
---
draft: false
date: 2024-02-20
categories:
  - DevLog
authors:
  - willmcgugan
---

# Remote memory profiling with Memray

[Memray](https://github.com/bloomberg/memray) is a memory profiler for Python, built by some very smart devs at Bloomberg.
It is a fantastic tool to identify memory leaks in your code or other libraries (down to the C level)!

They recently added a [Textual](https://github.com/textualize/textual/) interface which looks amazing, and lets you monitor your process right from the terminal:

![Memray](https://raw.githubusercontent.com/bloomberg/memray/main/docs/_static/images/live_animated.webp)

<!-- more -->

You would typically run this locally, or over a ssh session, but it is also possible to serve the interface over the web with the help of [textual-web](https://github.com/Textualize/textual-web).
I'm not sure if even the Memray devs themselves are aware of this, but here's how.

First install Textual web (ideally with pipx) alongside Memray:

```bash
pipx install textual-web
```

Now you can serve Memray with the following command (replace the text in quotes with your Memray options):

```bash
textual-web -r "memray run --live -m http.server"
```

This will return a URL you can use to access the Memray app from anywhere.
Here's a quick video of that in action:

<iframe style="aspect-ratio: 16 /10" width="100%" src="https://www.youtube.com/embed/7lpoUBdxzus" title="Serving Memray with Textual web" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Found this interesting?


Join our [Discord server](https://discord.gg/Enf6Z3qhVr) if you want to discuss this post with the Textual devs or community.



================================================
FILE: docs/blog/posts/responsive-app-background-task.md
================================================
---
draft: false
date: 2022-12-07
categories:
  - DevLog
authors:
  - rodrigo
---

# Letting your cook multitask while bringing water to a boil

Whenever you are cooking a time-consuming meal, you want to multitask as much as possible.
For example, you **do not** want to stand still while you wait for a pot of water to start boiling.
Similarly, you want your applications to remain responsive (i.e., you want the cook to “multitask”) while they do some time-consuming operations in the background (e.g., while the water heats up).

The animation below shows an example of an application that remains responsive (colours on the left still change on click) even while doing a bunch of time-consuming operations (shown on the right).

![](../images/2022-12-07-responsive-app-background-task/responsive-demo.gif)

In this blog post, I will teach you how to multitask like a good cook.

<!-- more -->


## Wasting time staring at pots

There is no point in me presenting a solution to a problem if you don't understand the problem I am trying to solve.
Suppose we have an application that needs to display a huge amount of data that needs to be read and parsed from a file.
The first time I had to do something like this, I ended up writing an application that “blocked”.
This means that _while_ the application was reading and parsing the data, nothing else worked.

To exemplify this type of scenario, I created a simple application that spends five seconds preparing some data.
After the data is ready, we display a `Label` on the right that says that the data has been loaded.
On the left, the app has a big rectangle (a custom widget called `ColourChanger`) that you can click and that changes background colours randomly.

When you start the application, you can click the rectangle on the left to change the background colour of the `ColourChanger`, as the animation below shows:

![](../images/2022-12-07-responsive-app-background-task/blocking01-colour-changer.gif)

However, as soon as you press `l` to trigger the data loading process, clicking the `ColourChanger` widget doesn't do anything.
The app doesn't respond because it is busy working on the data.
This is the code of the app so you can try it yourself:

```py hl_lines="11-13 21 35 36"
--8<-- "docs/blog/snippets/2022-12-07-responsive-app-background-task/blocking01.py"
```

1. The widget `ColourChanger` changes colours, randomly, when clicked.
2. We create a binding to the key `l` that runs an action that we know will take some time (for example, reading and parsing a huge file).
3. The method `action_load` is responsible for starting our time-consuming task and then reporting back.
4. To simplify things a bit, our “time-consuming task” is just standing still for 5 seconds.

I think it is easy to understand why the widget `ColourChanger` stops working when we hit the `time.sleep` call if we consider [the cooking analogy](https://mathspp.com/blog/til/cooking-with-asyncio) I have written about before in my blog.
In short, Python behaves like a lone cook in a kitchen:

 - the cook can be clever and multitask. For example, while water is heating up and being brought to a boil, the cook can go ahead and chop some vegetables.
 - however, there is _only one_ cook in the kitchen, so if the cook is chopping up vegetables, they can't be seasoning a salad.

Things like “chopping up vegetables” and “seasoning a salad” are _blocking_, i.e., they need the cook's time and attention.
In the app that I showed above, the call to `time.sleep` is blocking, so the cook can't go and do anything else until the time interval elapses.

## How can a cook multitask?

It makes a lot of sense to think that a cook would multitask in their kitchen, but Python isn't like a smart cook.
Python is like a very dumb cook who only ever does one thing at a time and waits until each thing is completely done before doing the next thing.
So, by default, Python would act like a cook who fills up a pan with water, starts heating the water, and then stands there staring at the water until it starts boiling instead of doing something else.
It is by using the module `asyncio` from the standard library that our cook learns to do other tasks while _awaiting_ the completion of the things they already started doing.

[Textual](https://github.com/textualize/textual) is an async framework, which means it knows how to interoperate with the module `asyncio` and this will be the solution to our problem.
By using `asyncio` with the tasks we want to run in the background, we will let the application remain responsive while we load and parse the data we need, or while we crunch the numbers we need to crunch, or while we connect to some slow API over the Internet, or whatever it is you want to do.

The module `asyncio` uses the keyword `async` to know which functions can be run asynchronously.
In other words, you use the keyword `async` to identify functions that contain tasks that would otherwise force the cook to waste time.
(Functions with the keyword `async` are called _coroutines_.)

The module `asyncio` also introduces a function `asyncio.create_task` that you can use to run coroutines concurrently.
So, if we create a coroutine that is in charge of doing the time-consuming operation and then run it with `asyncio.create_task`, we are well on our way to fix our issues.

However, the keyword `async` and `asyncio.create_task` alone aren't enough.
Consider this modification of the previous app, where the method `action_load` now uses `asyncio.create_task` to run a coroutine who does the sleeping:

```py hl_lines="36-37 39"
--8<-- "docs/blog/snippets/2022-12-07-responsive-app-background-task/blocking02.py"
```

1. The action method `action_load` now defers the heavy lifting to another method we created.
2. The time-consuming operation can be run concurrently with `asyncio.create_task` because it is a coroutine.
3. The method `_do_long_operation` has the keyword `async`, so it is a coroutine.

This modified app also works but it suffers from the same issue as the one before!
The keyword `async` tells Python that there will be things inside that function that can be _awaited_ by the cook.
That is, the function will do some time-consuming operation that doesn't require the cook's attention.
However, we need to tell Python which time-consuming operation doesn't require the cook's attention, i.e., which time-consuming operation can be _awaited_, with the keyword `await`.

Whenever we want to use the keyword `await`, we need to do it with objects that are compatible with it.
For many things, that means using specialised libraries:

 - instead of `time.sleep`, one can use `await asyncio.sleep`;
 - instead of the module `requests` to make Internet requests, use `aiohttp`; or
 - instead of using the built-in tools to read files, use `aiofiles`.

## Achieving good multitasking

To fix the last example application, all we need to do is replace the call to `time.sleep` with a call to `asyncio.sleep` and then use the keyword `await` to signal Python that we can be doing something else while we sleep.
The animation below shows that we can still change colours while the application is completing the time-consuming operation.

=== "Code"

    ```py hl_lines="40 41 42"
    --8<-- "docs/blog/snippets/2022-12-07-responsive-app-background-task/nonblocking01.py"
    ```

    1. We create a label that tells the user that we are starting our time-consuming operation.
    2. We `await` the time-consuming operation so that the application remains responsive.
    3. We create a label that tells the user that the time-consuming operation has been concluded.

=== "Animation"

    ![](../images/2022-12-07-responsive-app-background-task/non-blocking.gif)

Because our time-consuming operation runs concurrently, everything else in the application still works while we _await_ for the time-consuming operation to finish.
In particular, we can keep changing colours (like the animation above showed) but we can also keep activating the binding with the key `l` to start multiple instances of the same time-consuming operation!
The animation below shows just this:

![](../images/2022-12-07-responsive-app-background-task/responsive-demo.gif)

!!! warning

    The animation GIFs in this blog post show low-quality colours in an attempt to reduce the size of the media files you have to download to be able to read this blog post.
    If you run Textual locally you will see beautiful colours ✨



================================================
FILE: docs/blog/posts/rich-inspect.md
================================================
---
draft: false
date: 2023-07-27
categories:
  - DevLog
title: Using Rich Inspect to interrogate Python objects
authors:
  - willmcgugan
---

# Using Rich Inspect to interrogate Python objects

The [Rich](https://github.com/Textualize/rich) library has a few functions that are admittedly a little out of scope for a terminal color library. One such function is `inspect` which is so useful you may want to `pip install rich` just for this feature.

<!-- more -->

The easiest way to describe `inspect` is that it is Python's builtin `help()` but easier on the eye (and with a few more features).
If you invoke it with any object, `inspect` will display a nicely formatted report on that object &mdash; which makes it great for interrogating objects from the REPL. Here's an example:

```python
>>> from rich import inspect
>>> text_file = open("foo.txt", "w")
>>> inspect(text_file)
```

Here we're inspecting a file object, but it could be literally anything.
You will see the following output in the terminal:

<div>
--8<-- "docs/blog/images/inspect1.svg"
</div>

By default, `inspect` will generate a data-oriented summary with a text representation of the object and its data attributes.
You can also add `methods=True` to show all the methods in the public API.
Here's an example:

```python
>>> inspect(text_file, methods=True)
```

<div>
--8<-- "docs/blog/images/inspect2.svg"
</div>

The documentation is summarized by default to avoid generating verbose reports.
If you want to see the full unabbreviated help you can add `help=True`:

```python
>>> inspect(text_file, methods=True, help=True)
```

<div>
--8<-- "docs/blog/images/inspect3.svg"
</div>

There are a few more arguments to refine the level of detail you need (private methods, dunder attributes etc).
You can see the full range of options with this delightful little incantation:

```python
>>> inspect(inspect)
```

If you are interested in Rich or Textual, join our [Discord server](https://discord.gg/Enf6Z3qhVr)!


## Addendum

Here's how to have `inspect` always available without an explicit import:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Put this in your pythonrc file: <a href="https://t.co/pXTi69ykZL">pic.twitter.com/pXTi69ykZL</a></p>&mdash; Tushar Sadhwani (@sadhlife) <a href="https://twitter.com/sadhlife/status/1684446413785280517?ref_src=twsrc%5Etfw">July 27, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



================================================
FILE: docs/blog/posts/smooth-scrolling.md
================================================
---
draft: false
date: 2025-02-16
categories:
  - DevLog
authors:
  - willmcgugan
---

# Smoother scrolling in the terminal &mdash; a feature decades in the making

The great philosopher F. Bueller once said “Life moves pretty fast. If you don't stop and look around once in a while, you could miss it.”

Beuller was *not* taking about terminals, which tend not to move very fast at all.
Until they do.
From time to time terminals acquire new abilities after a long plateau.
We are now seeing a kind of punctuated evolution in terminals which makes things possible that just weren't feasible a short time ago.

I want to talk about one such feature, which *I believe* has been decades[^1] in the making.
Take a look at the following screen recording (taken from a TUI running in the terminal):

![A TUI Scrollbar](../images/smooth-scroll/no-smooth-scroll.gif)

<!-- more -->

Note how the mouse pointer moves relatively smoothly, but the scrollbar jumps with a jerky motion.

This happens because the terminal reports the mouse coordinates in cells (a *cell* is the dimensions of a single latin-alphabet character).
In other words, the app knows only which cell is under the pointer.
It isn't granular enough to know where the pointer is *within* a cell.

Until recently terminal apps couldn't do any better.
More granular mouse reporting is possible in the terminal; write the required escape sequence and mouse coordinates are reported in pixels rather than cells.

So why haven't TUIs been using this?

The problem is that pixel coordinates are pretty much useless in TUIs unless we have some way of translating between pixel and cell coordinates.
Without that, we can never know which cell the user clicked on.

It's a trivial calculation, but we are missing a vital piece of information; the size of the terminal window in pixels.
If we had that, we could divide the pixel dimensions by the cell dimensions to calculate the pixels per cell.
Divide pixel coordinates by *pixels per cell* and we have cell coordinates.

But the terminal reports its size in cells, and *not* pixels.
So we can't use granular mouse coordinates.

!!! question "What did people use pixel coordinate for?"

    This does make we wonder what pixel reporting was ever used for in terminals.
    Ping me on Discord if you know!


At least we couldn't until [this recent extension](https://gist.github.com/rockorager/e695fb2924d36b2bcf1fff4a3704bd83) which reports the size of the terminal in cell *and* pixel coordinates.
Once we have both the mouse coordinates in pixels and the dimensions of the terminal in pixels, we can implement much smoother scrolling.

Let's see how this looks.

On the left we have the default scrolling, on the right, Textual is using granular mouse coordinates.


| Default scrolling                                                | Smooth scrolling                                                                    |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| ![A TUI Scrollbar](../images/smooth-scroll/no-smooth-scroll.gif) | ![A TUI Scrollbar with smooth scrolling](../images/smooth-scroll/smooth-scroll.gif) |

Notice how much smoother the motion of the table is, now that it tracks the mouse cursor more accurately.

If you have one of the terminals which support this feature[^2], and at least [Textual](https://github.com/textualize/textual/) 2.0.0 you will be able to see this in action.

I think Textual may be the first library to implement this.
Let me know, if you have encountered any non-Textual TUI app which implements this kind of smooth scrolling.

## Join us

Join our [Discord server](https://discord.gg/Enf6Z3qhVr) to discuss anything terminal related with the Textualize devs, or the community!


[^1]: I'm not sure exactly when pixel mouse reporting was added to terminals. I'd be interested if anyone has a precised date.
[^2]: Kitty, Ghostty, and a few others.



================================================
FILE: docs/blog/posts/spinners-and-pbs-in-textual.md
================================================
---
draft: false
date: 2022-11-24
categories:
  - DevLog
authors:
  - rodrigo
---

# Spinners and progress bars in Textual

![](../images/spinners-and-pbs-in-textual/live-display.gif)

One of the things I love about mathematics is that you can solve a problem just by **guessing** the correct answer.
That is a perfectly valid strategy for solving a problem.
The only thing you need to do after guessing the answer is to prove that your guess is correct.

I used this strategy, to some success, to display spinners and indeterminate progress bars from [Rich](github.com/textualize/rich) in [Textual](https://github.com/textualize/textual).

<!-- more -->


## Display an indeterminate progress bar in Textual

I have been playing around with Textual and recently I decided I needed an indeterminate progress bar to show that some data was loading.
Textual is likely to [get progress bars in the future](https://github.com/Textualize/rich/issues/2665#issuecomment-1326229220), but I don't want to wait for the future!
I want my progress bars now!
Textual builds on top of Rich, so if [Rich has progress bars](https://rich.readthedocs.io/en/stable/progress.html), I reckoned I could use them in my Textual apps.


### Progress bars in Rich

Creating a progress bar in Rich is as easy as opening up the documentation for `Progress` and copying & pasting the code.


=== "Code"

    ```py
    import time
    from rich.progress import track

    for _ in track(range(20), description="Processing..."):
        time.sleep(0.5)  # Simulate work being done
    ```

=== "Output"

    ![](../images/spinners-and-pbs-in-textual/rich-progress-bar.gif)


The function `track` provides a very convenient interface for creating progress bars that keep track of a well-specified number of steps.
In the example above, we were keeping track of some task that was going to take 20 steps to complete.
(For example, if we had to process a list with 20 elements.)
However, I am looking for indeterminate progress bars.

Scrolling further down the documentation for `rich.progress` I found what I was looking for:

=== "Code"

    ```py hl_lines="5"
    import time
    from rich.progress import Progress

    with Progress() as progress:
        _ = progress.add_task("Loading...", total=None)  # (1)!
        while True:
            time.sleep(0.01)
    ```

    1. Setting `total=None` is what makes it an indeterminate progress bar.

=== "Output"

    ![](../images/spinners-and-pbs-in-textual/indeterminate-rich-progress-bar.gif)

So, putting an indeterminate progress bar on the screen is _easy_.
Now, I only needed to glue that together with the little I know about Textual to put an indeterminate progress bar in a Textual app.


### Guessing what is what and what goes where

What I want is to have an indeterminate progress bar inside my Textual app.
Something that looks like this:

![](../images/spinners-and-pbs-in-textual/bar-in-textual.gif)

The GIF above shows just the progress bar.
Obviously, the end goal is to have the progress bar be part of a Textual app that does something.

So, when I set out to do this, my first thought went to the stopwatch app in the [Textual tutorial](https://textual.textualize.io/tutorial) because it has a widget that updates automatically, the `TimeDisplay`.
Below you can find the essential part of the code for the `TimeDisplay` widget and a small animation of it updating when the stopwatch is started.


=== "`TimeDisplay` widget"

    ```py hl_lines="14 18 22"
    from time import monotonic

    from textual.reactive import reactive
    from textual.widgets import Static


    class TimeDisplay(Static):
        """A widget to display elapsed time."""

        start_time = reactive(monotonic)
        time = reactive(0.0)
        total = reactive(0.0)

        def on_mount(self) -> None:
            """Event handler called when widget is added to the app."""
            self.update_timer = self.set_interval(1 / 60, self.update_time, pause=True)

        def update_time(self) -> None:
            """Method to update time to current."""
            self.time = self.total + (monotonic() - self.start_time)

        def watch_time(self, time: float) -> None:
            """Called when the time attribute changes."""
            minutes, seconds = divmod(time, 60)
            hours, minutes = divmod(minutes, 60)
            self.update(f"{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}")
    ```

=== "Output"

    ![](../images/spinners-and-pbs-in-textual/stopwatch-timedisplay.gif)


The reason the time display updates magically is due to the three methods that I highlighted in the code above:

 1. The method `on_mount` is called when the `TimeDisplay` widget is mounted on the app and, in it, we use the method `set_interval` to let Textual know that every `1 / 60` seconds we would like to call the method `update_time`. (In other words, we would like `update_time` to be called 60 times per second.)
 2. In turn, the method `update_time` (which is called _automatically_ a bunch of times per second) will update the reactive attribute `time`. _When_ this attribute update happens, the method `watch_time` kicks in.
 3. The method `watch_time` is a watcher method and gets called whenever the attribute `self.time` is assigned to.
 So, if the method `update_time` is called a bunch of times per second, the watcher method `watch_time` is also called a bunch of times per second. In it, we create a nice representation of the time that has elapsed and we use the method `update` to update the time that is being displayed.

I thought it would be reasonable if a similar mechanism needed to be in place for my progress bar, but then I realised that the progress bar seems to update itself...
Looking at the indeterminate progress bar example from before, the only thing going on was that we used `time.sleep` to stop our program for a bit.
We didn't do _anything_ to update the progress bar...
Look:

```py
with Progress() as progress:
    _ = progress.add_task("Loading...", total=None)  # (1)!
    while True:
        time.sleep(0.01)
```

After pondering about this for a bit, I realised I would not need a watcher method for anything.
The watcher method would only make sense if I needed to update an attribute related to some sort of artificial progress, but that clearly isn't needed to get the bar going...

At some point, I realised that the object `progress` is the object of interest.
At first, I thought `progress.add_task` would return the progress bar, but it actually returns the integer ID of the task added, so the object of interest is `progress`.
Because I am doing nothing to update the bar explicitly, the object `progress` must be updating itself.

The Textual documentation also says that we can [build widgets from Rich renderables](https://textual.textualize.io/guide/widgets/#rich-renderables), so I concluded that if `Progress` were a renderable, then I could inherit from `Static` and use the method `update` to update the widget with my instance of `Progress` directly.
I gave it a try and I put together this code:

```py hl_lines="10 11 15-17 20"
from rich.progress import Progress, BarColumn

from textual.app import App, ComposeResult
from textual.widgets import Static


class IndeterminateProgress(Static):
    def __init__(self):
        super().__init__("")
        self._bar = Progress(BarColumn())  # (1)!
        self._bar.add_task("", total=None)  # (2)!

    def on_mount(self) -> None:
        # When the widget is mounted start updating the display regularly.
        self.update_render = self.set_interval(
            1 / 60, self.update_progress_bar
        )  # (3)!

    def update_progress_bar(self) -> None:
        self.update(self._bar)  # (4)!


class MyApp(App):
    def compose(self) -> ComposeResult:
        yield IndeterminateProgress()


if __name__ == "__main__":
    app = MyApp()
    app.run()
```

 1. Create an instance of `Progress` that just cares about the bar itself (Rich progress bars can have a label, an indicator for the time left, etc).
 2. We add the indeterminate task with `total=None` for the indeterminate progress bar.
 3. When the widget is mounted on the app, we want to start calling `update_progress_bar` 60 times per second.
 4. To update the widget of the progress bar we just call the method `Static.update` with the `Progress` object because `self._bar` is a Rich renderable.

And lo and behold, it worked:

![](../images/spinners-and-pbs-in-textual/bar-in-textual.gif)


### Proving it works

I finished writing this piece of code and I was ecstatic because it was working!
After all, my Textual app starts and renders the progress bar.
And so, I shared this simple app with someone who wanted to do a similar thing, but I was left with a bad taste in my mouth because I couldn't really connect all the dots and explain exactly why it worked.

!!! warning "Plot twist"

    By the end of the blog post, I will be much closer to a full explanation!


## Display a Rich spinner in a Textual app

A day after creating my basic `IndeterminateProgress` widget, I found someone that was trying to display a Rich spinner in a Textual app.
Actually, it was someone that had [filed an issue against Rich](https://github.com/Textualize/rich/issues/2665).
They didn't ask “how can I display a Rich spinner in a Textual app?”, but they filed an alleged bug that crept up on them _when_ they tried displaying a spinner in a Textual app.

When reading the issue I realised that displaying a Rich spinner looked very similar to displaying a Rich progress bar, so I made a tiny change to my code and tried to run it:

=== "Code"

    ```py hl_lines="10"
    from rich.spinner import Spinner

    from textual.app import App, ComposeResult
    from textual.widgets import Static


    class SpinnerWidget(Static):
        def __init__(self):
            super().__init__("")
            self._spinner = Spinner("moon")  # (1)!

        def on_mount(self) -> None:
            self.update_render = self.set_interval(1 / 60, self.update_spinner)

        def update_spinner(self) -> None:
            self.update(self._spinner)


    class MyApp(App[None]):
        def compose(self) -> ComposeResult:
            yield SpinnerWidget()


    MyApp().run()
    ```

    1. Instead of creating an instance of `Progress`, we create an instance of `Spinner` and save it so we can call `self.update(self._spinner)` later on.

=== "Spinner running"

    ![](../images/spinners-and-pbs-in-textual/spinner.gif)


## Losing the battle against pausing the animations

After creating the progress bar and spinner widgets I thought of creating the little display that was shown at the beginning of the blog post:

![](../images/spinners-and-pbs-in-textual/live-display.gif)

When writing the code for this app, I realised both widgets had a lot of shared code and logic and I tried abstracting away their common functionality.
That led to the code shown below (more or less) where I implemented the updating functionality in `IntervalUpdater` and then let the `IndeterminateProgressBar` and `SpinnerWidget` instantiate the correct Rich renderable.

```py hl_lines="8-15 22 30"
from rich.progress import Progress, BarColumn
from rich.spinner import Spinner

from textual.app import RenderableType
from textual.widgets import Button, Static


class IntervalUpdater(Static):
    _renderable_object: RenderableType  # (1)!

    def update_rendering(self) -> None:  # (2)!
        self.update(self._renderable_object)

    def on_mount(self) -> None:  # (3)!
        self.interval_update = self.set_interval(1 / 60, self.update_rendering)


class IndeterminateProgressBar(IntervalUpdater):
    """Basic indeterminate progress bar widget based on rich.progress.Progress."""
    def __init__(self) -> None:
        super().__init__("")
        self._renderable_object = Progress(BarColumn())  # (4)!
        self._renderable_object.add_task("", total=None)


class SpinnerWidget(IntervalUpdater):
    """Basic spinner widget based on rich.spinner.Spinner."""
    def __init__(self, style: str) -> None:
        super().__init__("")
        self._renderable_object = Spinner(style)  # (5)!
```

 1. Instances of `IntervalUpdate` should set the attribute `_renderable_object` to the instance of the Rich renderable that we want to animate.
 2. The methods `update_rendering` and `on_mount` are exactly the same as what we had before, both in the progress bar widget and in the spinner widget.
 3. The methods `update_rendering` and `on_mount` are exactly the same as what we had before, both in the progress bar widget and in the spinner widget.
 4. For an indeterminate progress bar we set the attribute `_renderable_object` to an instance of `Progress`.
 5. For a spinner we set the attribute `_renderable_object` to an instance of `Spinner`.

But I wanted something more!
I wanted to make my app similar to the stopwatch app from the terminal and thus wanted to add a “Pause” and a “Resume” button.
These buttons should, respectively, stop the progress bar and the spinner animations and resume them.

Below you can see the code I wrote and a short animation of the app working.


=== "App code"

    ```py hl_lines="18-19 21-22 60-70 55-56"
    from rich.progress import Progress, BarColumn
    from rich.spinner import Spinner

    from textual.app import App, ComposeResult, RenderableType
    from textual.containers import Grid, Horizontal, Vertical
    from textual.widgets import Button, Static


    class IntervalUpdater(Static):
        _renderable_object: RenderableType

        def update_rendering(self) -> None:
            self.update(self._renderable_object)

        def on_mount(self) -> None:
            self.interval_update = self.set_interval(1 / 60, self.update_rendering)

        def pause(self) -> None:  # (1)!
            self.interval_update.pause()

        def resume(self) -> None:  # (2)!
            self.interval_update.resum
