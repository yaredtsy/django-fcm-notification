import firebase_admin

credentials = firebase_admin.credentials.Certificate('./test_firebase.JSON')
firebase_admin.initialize_app(credentials)
