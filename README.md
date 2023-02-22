# PuppetBlocks

[![Deploy for GitHub Pages - Website](https://github.com/CodingBlocks5/PuppetBlocks/actions/workflows/website.yml/badge.svg)](https://github.com/CodingBlocks5/PuppetBlocks/actions/workflows/website.yml)
[![Vulnerabilities Check (CodeQL) - Security](https://github.com/CodingBlocks5/PuppetBlocks/actions/workflows/vulnerabilities.yml/badge.svg)](https://github.com/CodingBlocks5/PuppetBlocks/actions/workflows/vulnerabilities.yml)
[![GitHub](https://img.shields.io/github/license/CodingBlocks5/PuppetBlocks)](https://github.com/CodingBlocks5/PuppetBlocks/blob/main/LICENSE)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/CodingBlocks5/PuppetBlocks)](https://github.com/CodingBlocks5/PuppetBlocks/releases)
[![GitHub repo size](https://img.shields.io/github/repo-size/CodingBlocks5/PuppetBlocks)](https://github.com/CodingBlocks5/PuppetBlocks)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fcodingblocks5.github.io%2FPuppetBlocks%2F)](https://codingblocks5.github.io/PuppetBlocks/)


[![logo](/assets/cover.jpg)](https://github.com/CodingBlocks5/PuppetBlocks)

## About the Project

Computer programming education in elementary schools in Israel is constantly rising. As most
of the textual programming languages are based on the English language, as well as they have
strict syntax requirements, elementary school student face many difficulties using them. In
order to overcome these challenges, we suggest using a simple visual programming language,
called "PuppetBlocks", for programming an interactive puppet, made by ESP32 micro-controller
and MicroPython firmware. By using Google Blockly library with BIPES platform, such a puppet
can be used for teaching both the concepts of algorithmic thinking and the basics of
programming in Python.

This project is based on a [previous work](https://github.com/BIPES/BIPES), by A. G. D. S. Junior
et. al. (2020). In this work, a framework for website-based visual programming language for
controlling micro-controllers using MicroPython firmware was presented. Please read the paper
for more details about this work:

> Junior, Andouglas Gonçalves Da Silva et. al. 2020. “<span class="nocase">
> BIPES: Block Based Integrated Platform for Embedded Systems</span>.” In IEEE Access,
> volume 8, pages 197955-197968..
> <https://doi.org/10.1109/ACCESS.2020.3035083>.

This work is submitted as the final project in the course "Project in The Internet of Things"
(236333), at The Interdisciplinary Center for Smart Technologies (ICST), Taub Faculty of
Computer Science, Technion - Israel Institute of Technology. This project was written by
Orel Adivi `(orel.adivi [at] cs.technion.ac.il)`, Hila Ginzburg
`(hila.gin [at] campus.technion.ac.il)`, and Noy Shmueli `(noyshmueli [at] campus.technion.ac.il)`,
and under the supervision of Assel Aborokn, Tom Sofer, and Itai Dabran, Ph.D. . The work was done in about
an academic semester and is released under GNU General Public License v3.0.


## Hardware
[![connections](/Hardware/connections.png)](https://github.com/CodingBlocks5/PuppetBlocks/blob/main/hardware/connections.png)


## Firmware

?

## Website

The main way in which the elementary school students interact with the system is using the website, available
on [https://codingblocks5.github.io/PuppetBlocks/](https://codingblocks5.github.io/PuppetBlocks/). This is a static,
single page frontend-based website, written in HTML, CSS, and JavaScript, allowing the students to program the
micro-controller. Beside the general blocks that were presented in BIPES, there are 31 unique blocks intend to
help the student interact with the device.

The following block categories were added:
- **Movement** - these blocks are used to control the two servo motors, read the joystick, record movements and
performing them.
- **Screens** - these blocks are used to control the two screens independently, allowing showing images and text 
and providing fast whitening and blacking function.
- **Audio** - these blocks are used to control the speaker, allowing playing audio synchronously or asynchronously,
once or in loop, and providing easy functions for pausing, resuming, stopping, and checking whether the speaker is
currently playing.
- **Files** - these blocks are used to load files from the cloud to the device, to check whether a file exists, to
delete a file on the device, to rename a file on the device, and to get a list of all currently available files on
the device.
- **Time** - these blocks are used to sleep for a specified time or until a specified time, to get the current time
or get a unit of it, and to do basic arithmetical calculations connected with time.

Downloading files to the device require previous uploading to the PuppetBlocks cloud, which is stored in Cloud
Storage for Firebase. The website allows a simple uploading and viewing a list of all currently available files
in the cloud. Executing the code is possible either using a serial (USB) connection or using WiFi with MicroPython
WebREPL. It is possible to download the current code to a local file and to upload previously downloaded files
from the local computer. The interface is available on English, with a basic support for Hebrew, Arabic, Italian,
and Russian.


## Project Engineering

For security purposes, commits were signed cryptographically, security Github Actions were enabled, and a
[SECURITY.md](https://github.com/CodingBlocks5/PuppetBlocks/blob/main/SECURITY.md) file was written. For documentation, a
[SUPPORT.md](https://github.com/CodingBlocks5/PuppetBlocks/blob/main/SUPPORT.md) file was written. The project was written using
both Visual Studio Code and Thonny IDE, and was managed using [GitHub](https://github.com/CodingBlocks5/PuppetBlocks).

For allowing an easier development, the following Github Actions were set, running on Linux (Ubuntu 20.04).:
1) **[Website](https://github.com/CodingBlocks5/PuppetBlocks/actions/workflows/website.yml)** - the
[PuppetBlocks website](https://codingblocks5.github.io/PuppetBlocks/) is updated with the current information.
2) **[Vulnerabilities check](https://github.com/CodingBlocks5/PuppetBlocks/actions/workflows/vulnerabilities.yml)** - the
updated code is checked to ensure it does not contain any known vulnerability.
3) **[Dependency review](https://github.com/CodingBlocks5/PuppetBlocks/actions/workflows/dependency-review.yml)** - the
dependencies are reviewed to check for any security issues.
4) **[Dependabot](https://github.com/CodingBlocks5/PuppetBlocks/blob/main/.github/dependabot.yml)** - the
dependency versions (in
[requirements.txt](https://github.com/CodingBlocks5/PuppetBlocks/blob/main/firmware/requirements.txt)) are updated regularly.

Please feel free to contact us with any questions you have about PuppetBlocks.
