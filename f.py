from flask import Flask,jsonify,request


#créer l'application Flask
app=Flask(__name__  )


#liste des étudiants
students=[
    {'id':1,'name':'Alice','age':20},
    {'id':2,'name':'Bob','age':22},]




#Endpoint pour obtenir la liste des étudiants
@app.route('/students',methods=['GET'])
def get_students():
    #jsonif transforme les données Python en JSON
    return jsonify(students)

#Endpoint pour ajouter un nouvel étudiant
@app.route('/students',methods=['POST'])
def add_student():
    new_student=request.get_json() #récupérer les données JSON de la requête
    new_student['id']=len(students)+1  #attribuer un nouvel id
    students.append(new_student)   #ajouter le nouvel étudiant à la liste
    return jsonify(new_student),201  #retourner le nouvel étudiant avec code 201 (créé)




#racine de l'api
@app.route('/')
def home():
    return "Bienvenue dans l'api des étudiants!"


#Activer mode debug pour voir les erreurs et recharger automatiquement le serveur 
if __name__=='__main__':
    app.run(debug=True)     




#serializer les données des étudiants en JSON ?
#déserializer les données JSON reçues en objets Python ?
#api REST / Framework 