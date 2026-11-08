# Periodic (Evo Edition) 

A clean, fast Periodic table app for the TI-84 Evo, written in MicroPython.


## ⚠⚠ IMPORTANT HARDWARE REQUIREMENT

> **READ BEFORE RUNNING:**
> This app is optimized specifically for the TI-84 Evo (ARM Cortex M33 @ 156MHz).
> 
> ~~While it still runs on the TI-84 Plus CE **Python** (eZ80 @ 48MHz), performance will be very slow due to low execution speed on less capable silicon(And in that case, you don't even need this app since it already has a native app). If it's unusable on your calculator, your hardware just isn't fast enough. You have been warned!~~
> Actually, I take that back, it won't even run at all!\
> <small>Why don't someone go ahead and test the app on the TI-Nspire and tell me if it works or not? 😛</small>

## Installation and Usage

1. Connect your TI-84 Evo/Plus CE into your computer via USB.
2. Open webTiLP or TI-Connect Evo site in your prefered web browser(TI's site requires Chrome)
3. Optionally, minify PERIODIC.py and then send it to your calculator.
4. Once sent, on your calculator, press the `prgm` key, select the Python App then PERIODIC, and press `enter`.
5. Alternatively, run the binary in the .zip file in the Releases for a prepackaged emulator for desktop.

### Controls
- **Arrow Keys**: Navigate the table and scroll the details page.
- **Enter**: Opens expanded element properties page from table.
- **Softkeys**: Uses the top keys of the keypad (y=, window, zoom, trace, graph) for navigation. 

## Features

- **118-Element Dataset**: Complete data including atomic mass, electron config, and more!
- **Faithful CE-style UI**: Ported over the style of the CE's Periodic Table layout and navigation system from scratch.
- **Zero Dependencies**: Everything is programmatically drawn with no need for extra image appvars.

## AI Attribution

- **AI used**: Google Gemini
- **Scope**: Generated and structured the 118-element data array (`E`) and acted as a technical  partner for debugging
- **From Me**: Everything else!

## ToDo list
- ~~Add list of elements so students can find element quickly~~ Done!
- Add graphs of data just to copy TI's useless feature
- ~~Roast TI for breaking backwards compatibility for every appvar format and programs(well, besides Python, of course)~~ In progress in the form of a jailbreak 😁
