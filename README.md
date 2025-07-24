<div align="center">

# Message Paster

Message Paster is a simple yet powerful tool for assigning custom keybinds to frequently used messages. The application allows you to send predefined messages to any text field by simply pressing the corresponding keybind. It uses Python's `pyautogui` for simulating keystrokes and `keyboard` for capturing hotkeys.

![Message Paster](https://github.com/user-attachments/assets/593623bf-17c7-47d6-a056-74aa25b6954f)

</div>

## Features

- Assign custom keybinds to predefined messages.
- Adjust typing speed with a user-friendly slider.
- Easily load and save keybind configurations and messages in JSON format.
- Intuitive graphical user interface built with Tkinter.
- Threaded execution for sending messages, ensuring smooth performance without blocking other actions.

<div align="center">

## ☕ [Support my work on Ko-Fi](https://ko-fi.com/thatsinewave)

</div>

## Installation

1. Clone or download the repository.
2. Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

   The dependencies are:
   - `keyboard`: for managing hotkeys.
   - `pyautogui`: for simulating typing.
   - `tkinter`: for creating the graphical interface.
   - `json`: for reading and writing configuration files.

## Usage

1. Run the `paster.py` script:

   ```bash
   python paster.py
   ```

2. The window will open, allowing you to configure the keybinds and typing speed.

3. For each message, you can click on it to assign a keybind. If a key is already assigned, you will be prompted with a warning.

4. Adjust the typing speed using the slider for faster or slower typing.

5. Once the keybinds are set up, press the assigned keys to send the corresponding message to the currently focused text field.

## Configuration Files

- **keybinds.json**: Stores the keybinds for each message.
  - Example format:
    ```json
    {
        "Message 1": "F1",
        "Message 2": "F2"
    }
    ```
- **messages.json**: Stores the predefined messages that can be assigned to keybinds.
  - Example format:
    ```json
    {
        "Message 1": "[Placeholder]",
        "Message 2": "[Another Placeholder]"
    }
    ```

## Customization

You can edit `messages.json` to change the predefined messages and `keybinds.json` to manage your key assignments.

## Troubleshooting

- If the program doesn't detect the keypresses, ensure you have the required permissions to listen for keyboard events, especially on Linux or macOS.
- If you encounter issues with the message sending, verify that the correct application or text field is focused.

<div align="center">

## [Join my discord server](https://thatsinewave.github.io/Discord-Redirect/)

</div>

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
