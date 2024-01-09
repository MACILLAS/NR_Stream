# Flask Socketio GUI Test

This is to test capabilities of Flask-Socketio
to facilitate communication between a webclient and Python-Flask server.

## Implemented Features

- [x] Semi-persistence (session)
- [x] Error handling w/ feedback
- [x] Page redirect
- [x] Inaccessible viewer page without existing session
- [x] Server send image to viewer based on selected model
- [x] Server listens for DOM keypress events
- [x] Dynamically sized canvas based on image size
- [x] Draw a line on canvas

## Future Features
- [ ] Calculate new-camera from keypress events
- [ ] Server emit new rendered image to client
- [ ] Increase GUI functionality
  -[ ] Mouse control
  - [ ] Speed toggle and other options
- [ ] Twin models
- [ ] Toggle which model to control
- [ ] Retrieve closest images