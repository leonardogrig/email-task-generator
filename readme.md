# Email Task Generator

This application analyzes emails and generates tasks based on their content. It uses AI to determine if an email should become a task, its urgency, and other relevant details.

## Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerized setup)

## Getting Started

### Running with Docker (Recommended)

1. Make sure you have Docker and Docker Compose installed on your system.

2. Clone this repository and navigate to the project directory.

3. Build and run the Docker container:

   ```
   docker-compose up --build
   ```

4. The application will be available at `http://localhost:5000`.

### Running without Docker

1. Clone this repository and navigate to the project directory.

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables:

   - Create a `.env` file in the /app folder
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

5. Run the application:

   ```
   python app/app.py
   ```

6. The application will be available at `http://localhost:5000`.

## Usage

Send a POST request to `/analyze_emails` with a JSON payload containing an array of email objects. Each email object should have the following structure:

```json
{
  "subject": "Email subject",
  "from": "sender@example.com",
  "date": "2024-08-20T10:00:00Z",
  "snippet": "Brief preview of the email content",
  "body": "Full body of the email"
}
```

The API will return an array of analyzed emails with AI-generated task information.

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or bug fixes to suggest.

## License

[MIT License](LICENSE)
