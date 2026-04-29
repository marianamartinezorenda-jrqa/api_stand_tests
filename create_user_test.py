import sender_stand_request
import data

def get_user_body (first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

#Prueba 1: creación de usuario con nombre de 2 caracteres
def test_create_user_2_letter_in_first_name_get_success_response(first_name):
    user_body = get_user_body("Aa")
    user_response = sender_stand_request.post_create_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

#prueba 2: Usuario con 15 caracteres.
def test_create_user_15_letter_in_first_name_get_success_response(fist_name):
    user_body = get_user_body("Aaaaaaaaaaaaaaa")
    positive_assert = (user_body)
    user_response = sender_stand_request.post_create_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

#Prueba 3: Número de caracteres menor a la permitida (1)
def negative_assert_symbol(first_name):
    user_body = get_user_body("A")
    negative_assert_symbol(user_body)
    response = sender_stand_request.post_create_new_user(user_body)
    assert response.status_code == 400
    assert response.json() ["code"] == 400
    assert response.json() ["message"] == "Has introducido un nombre de usuario no válido" \
                                            "El nombre solo puede contener letras del alfabeto latino, " \
                                            "la longitud debe ser de 2 a 15 caracteres."

#Prueba 4: Número de caracteres: 16 en el first name = ERROR
def test_create_user_16_letter_in_first_name_get_error_response(first_name):
    user_body = get_user_body("Aaaaaaaaaaaaaaaa")
    negative_assert_symbol(user_body)
    response = sender_stand_request.post_create_new_user(user_body)
    assert response.status_code == 400
    assert response.json() ["code"] == 400
    assert response.json() ["message"] == "Has introducido un nombre de usuario no válido" \
                                            "El nombre solo puede contener letras del alfabeto latino, " \
                                            "la longitud debe ser de 2 a 15 caracteres."

#Prueba 5: No se permiten espacios en el campo "first name"
def test_create_user_has_space_in_first_name_get_error_response(first_name):
    user_body = get_user_body("A Aaa")
    negative_assert_symbol(user_body)
    response = sender_stand_request.post_create_new_user(user_body)
    assert response.status_code == 400
    assert response.json() ["code"] == 400
    assert response.json()["message"] == "El nombre solo puede contener letras del alfabeto latino, " \
                                         "la longitud debe ser de 2 a 15 caracteres."

#Prueba 6: No se admiten caracteres especiales en el campo "first name"
def test_create_user_has_special_symbol_in_first_name_get_error_response(first_name):
    user_body = get_user_body(\"&%$/&"\)
    negative_assert_symbol(user_body)
    response = sender_stand_request.post_create_new_user(user_body)
    assert response.status_code == 400
    assert response.json() ["code"] == 400
    assert response.json() ["message"] == "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"

#Prueba 7: No se permiten números en el campo "first name".
def test_create_user_has_number_in_first_name_get_error_response(first_name):
    negative_assert_symbol("123")
    response = sender_stand_request.post_create_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"

#Prueba 8: The "first name" field was not send
def negative_assert_no_firstname(firs_name): #Aquí no se usa ni negative ni possitive assert porque el campo "no existe"
    response = sender_stand_request.post_create_new_user(user_body)
    assert response.status_code == 400
    assert response.json() ["code"] == 400
    assert response.json() ["message"] == "No se han aprobado todos los parámetros requeridos"

#Prueba 9: The "first name" field was send as an empty field
def test_create_user_empty_first_name_get_error_response(fist_name):
    user_body = get_user_body("")
    negative_assert_no_firstname(user_body)
    response = sender_stand_request.post_create_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se enviaron los parámetros requeridos"

#Prueba 10: Into the "first name" field there is an INT number
def test_create_user_number_type_first_name_get_error_response(first_name):
    user_body = get_user_body(12)
    negative_assert_no_firstname(user_body)
    response = sender_stand_request.post_create_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "El nombre solo puede contener letras latinas"