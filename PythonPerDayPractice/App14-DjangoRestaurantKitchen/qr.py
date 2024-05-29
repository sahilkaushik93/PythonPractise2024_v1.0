import qrcode

loc = 'E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice\App14-DjangoRestaurantKitchen'

image = qrcode.make("https://127.0.0.1:8000")

image.save(f"{loc}/app-qr.png")