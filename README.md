
# Paint Automation using Python

This code automates the process of painting an image using the paint application. The image is first downloaded from a URL and then converted to grayscale. The code then uses the `pyautogui` library to simulate mouse clicks and keyboard input to select colors and paint pixels on the canvas in the paint application.

## Required Libraries

-   `pyautogui`
-   `PIL` (Python Imaging Library)
-   `requests`
-   `io`
-   `pandas`

## Usage

1.  Open the paint application
2.  Make sure the canvas is selected and ready for painting
3.  Run the code
4.  The code will prompt you to press Enter when you're ready to start painting
5.  The painting process will begin and will be completed automatically

## Note

The code assumes that the paint application is open and set up for painting. The code also uses hardcoded screen coordinates for the paint application, which may need to be adjusted based on your screen resolution and setup.
