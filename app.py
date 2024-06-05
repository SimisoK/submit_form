from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Get the submitted PDF file
        pdf_file = request.files['pdf']
        # Save the file to a desired location
        pdf_file.save('submitted_forms/' + pdf_file.filename)
        
        # You can process the PDF here if needed

        return jsonify({'status': 'success', 'message': 'Form submitted successfully!'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
