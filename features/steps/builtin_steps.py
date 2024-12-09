from behave_webdriver.steps import * # ignore
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

@given('I open the url "{url}"')
def step_open_url(context, url):
    context.behave_driver.get(url)

@when('I input the text "{text}" in the input field')
def step_input_text(context, text):
    input_field = WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.ID, "letters"))
    )
    input_field.clear()
    input_field.send_keys(text)

@when('I set the shift to "{shift}"')
def step_set_shift(context, shift):
    shift_dropdown = WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.ID, "shift-amount"))
    )
    Select(shift_dropdown).select_by_value(shift)

@when('I click the "{button}" button')
def step_click_button(context, button):
    button_element = WebDriverWait(context.behave_driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    button_element.click()
    sleep(0.2)

@when('I set the mode to "{mode}"')
def step_set_mode(context, mode):
    mode_dropdown = WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.ID, "decoder-setting"))
    )
    Select(mode_dropdown).select_by_visible_text(mode)

@then('I should see the encoded message "{expected_message}"')
def step_verify_encoded_message(context, expected_message):
    result_text = WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.ID, "decoded_message"))
    ).find_element(By.TAG_NAME, "p").text

@then('I should see the message "{expected_message}"')
def step_verify_message(context, expected_message):
    result_text = WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.ID, "decoded_message"))
    ).find_element(By.TAG_NAME, "p").text
