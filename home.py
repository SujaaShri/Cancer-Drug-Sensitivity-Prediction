@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    smiles = data['smiles']
    cell_line = data['cell_line']

    # Convert SMILES + cell line to model input
    # x_drug, x_cell = preprocess(smiles, cell_line)
    # pred = model(x_drug, x_cell)
    # ic50_value = pred.item()
    ic50_value = 2.43  # Dummy placeholder for demo

    return jsonify({'ic50': ic50_value})
