import pickle
import porter
clf = pickle.load(open('model.pkl', 'rb'))
vec = pickle.load(open('vec.pkl', 'rb'))

email = open('sample/emailSample1.txt', 'r').read()
email_clean = porter.processEmail(email)
email_transformed = vec.transform([email_clean])
print(clf.predict(email_transformed))