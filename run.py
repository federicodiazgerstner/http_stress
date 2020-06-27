#!flask/bin/python
from main import app

#Do not add debug=True
# app.run(debug=True)

# app.run()
app.run(host='0.0.0.0', port=80, debug=False)



