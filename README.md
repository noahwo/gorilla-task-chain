> This project initially uses [Gorilla](https://github.com/ShishirPatil/gorilla) project to automate a process of multiple tasks executed by Gorilla in stages.

The project aims at testing (showcasing) the capability of API invocations of Gorilla.

### Initial idea

The `img->text` and `text->tran` are two parts done by two calls to Gorilla, following the following steps: _Failed, but the logic still applies._

1. Calls Gorilla API to explain the purpose of recognizing the image content. It then returns a solution to call another API for specific machine learning model to solve the specific problem. We take the code part and try to execute it to get the result of our first stage.
2. The wanted result from stage 1 is the content text, which is then used as the input for the second stage. The second stage is to translate the text to five different languages. The process follows the same logic as stage 1, executing code given by Gorilla. The result is the five translated text.
3. We save the code of two parts, and integrate them as one complete program.
4. The final output of such a process should be a complete workable program and the result of the translation.

### How it works

Functionality code in `src/main.py`, it prints out the returned code into `src/module1.py`. Execute `module1.py` to do the wanted tasks.
Remember to set the environment variables in `src/.env`.

If errors about uninstalled pip packages reported, add it in to the list `packages` in `src/package_install.py` and run it.

### Issues

1. The `img->text` code does not run successfully, config error.
2. Essay writing did not work cuz performence limitation. The mode was like 10 GB.
3. Code is not always executable.
4. The smoothest part so far was generating code for translation.
