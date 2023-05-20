# Writing Your Vows
## This is an application that helps you erite your wedding vows

It is built over the openai api quickstart tutorial
You can follow the steps below to set up the project locally

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.
    ```bash
   $ git clone https://github.com/srivhash/WritingYourVows
   ```
3. Navigate into the project directory:

   ```bash
   $ cd WritingYourVows/
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ flask run
   ```


You should be able to access the app at [http://localhost:5000](http://localhost:5000)! 
You should be able to access the output at [http://localhost:5000/result](http://localhost:5000)!

For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
