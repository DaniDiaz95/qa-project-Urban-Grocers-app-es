import data
import sender_stand_request


#Valcidacion de tests para la creacion de un Kit
#Funcion que cambia el contenido del cuerpo de la solicitud del parametro name
def get_kit_body(user_kit):
    current_kit = data.kit_body.copy()#la funcion que contiene el cuerpo de la solicitud se copia del archivo data
    current_kit["name"] = user_kit['name'] #se camia el valor del parametro name

    return current_kit

# Pruebas positivas
def positive_assert(user_kit):
    kit_body = get_kit_body(user_kit)
    kit_response = sender_stand_request.post_new_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == user_kit['name']


# Pruebas negativas
def negative_assert(user_kit):
    kit_body = get_kit_body(user_kit)
    kit_response = sender_stand_request.post_new_kit(kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()['name'] == user_kit['name']


#1er test
def test_create_kit_1_letter_in_first_name_get_success_response():
    positive_assert(data.lower_allowed_limit)

#2do test
def test_create_kit_511_letter_in_first_name_get_success_response():
    positive_assert(data.upper_allowed_limit)

#3er test
def test_that_the_number_of_characters_is_zero():
    negative_assert(data.number_of_characters_is_less_than_0)

#4to test
def test_that_the_number_of_characters_is_greater_than_allowed():
    negative_assert(data.number_of_characters_is_greater_than_allowed)

#5to test
def test_allowing_special_characters_in_kit_creation():
    positive_assert(data.special_characters_are_valid)

#6to test
def test_allowing_spaces_in_the_kit_build_name():
    positive_assert(data.spaces_are_allowed)

#7mo test
def test_allowing_numbers_in_the_kit_creation_name():
    positive_assert(data.numbers_are_allowed)

#8vo test
def test_the_parameter_is_not_passed_in_the_function():
    kit_response = sender_stand_request.post_new_kit(data.kit_body_empty)

    assert kit_response.status_code == 400

#9no test
def test_that_does_not_allow_a_different_type_of_parameter():
    negative_assert(data.a_different_parameter_is_passed)

