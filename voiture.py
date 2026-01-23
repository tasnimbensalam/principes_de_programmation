from flask import Flask, jsonify, request

# Créer l'application Flask
app = Flask(__name__)

# Liste des voitures (simule une base de données)
cars = [
    {'id': 1, 'brand': 'Toyota', 'model': 'Corolla', 'year': 2020},
    {'id': 2, 'brand': 'Ford', 'model': 'Focus', 'year': 2019},
]

# -------------------- ENDPOINTS --------------------

# Racine de l'API
@app.route('/')
def home():
    return "Bienvenue dans l'API des voitures !"

# Obtenir la liste de toutes les voitures
@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)

# Ajouter une nouvelle voiture
@app.route('/cars', methods=['POST'])
def add_car():
    new_car = request.get_json()           # Récupérer les données JSON de la requête
    new_car['id'] = len(cars) + 1         # Attribuer un nouvel ID
    cars.append(new_car)                   # Ajouter à la liste
    return jsonify(new_car), 201           # Retourner la voiture créée avec code 201

# Obtenir une voiture par son ID
@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car = next((c for c in cars if c['id'] == car_id), None)
    if car:
        return jsonify(car)
    return jsonify({'message': 'Voiture non trouvée'}), 404

# Mettre à jour une voiture par son ID
@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    car = next((c for c in cars if c['id'] == car_id), None)
    if not car:
        return jsonify({'message': 'Voiture non trouvée'}), 404
    
    data = request.get_json()   # Données envoyées par le client
    car.update(data)            # Mise à jour des infos
    return jsonify(car)

# Supprimer une voiture par son ID
@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    global cars
    cars = [c for c in cars if c['id'] != car_id]
    return jsonify({'message': 'Voiture supprimée'})

# -------------------- LANCER L'APPLICATION --------------------
if __name__ == '__main__':
    app.run(debug=True)
