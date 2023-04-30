# StatusBarX

StatusBarX is a mini-application for MacOS (with MacBook Pro support on Intel) which displays CPU and GPU load as a percentage in the status bar. The application is written in Python 3.9.16 using the psutil and rumps libraries. The project is developed using a virtual environment.

## Features

- CPU load percentage display
- Display GPU load percentage
- Integration into MacOS status bar (tested on Intel Macbook Pro)

## Installation

Follow these steps to install the project dependencies:

1. Clone the repository:

```bash
   git clone git@github.com:Voolee/StatusBarX.git
   cd StatusBarX
```

2. Create and activate the virtual environment:

```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install the required libraries:

```bash
   pip install -r requirements.txt
```

## Run

After installing all the dependencies, run the application with the following command:

```bash
   python main.py
```

The application will start and you will see the CPU and GPU load percentage in the status bar of your computer.

## Collaboration

Pull-requests are welcome. If you have suggestions for improving the project, please create an issue.

## License

This project is licensed under the MIT License - see the LICENSE file for details.