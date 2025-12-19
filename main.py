import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from opencage.geocoder import OpenCageGeocode
import folium

def target(nomer):

    try:
        number = phonenumbers.parse(nomer, "id")

        if not phonenumbers.is_valid_number(number):
            input("Nomer Target tidak di Temukan ")

        internasional = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        nasional = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL)

        operator = carrier.name_for_number(number, "id")
        negara = geocoder.description_for_number(number, "id")

        key = "af9fde0403cd4d19a5a5098ecd07f1ce"
        geocoder = OpenCageGeocode(key)
        qerty = str(negara)
        result = geocoder.geocode(qerty)

        lat = result[0]["geometry"]["lat"]
        lng = result[0]["geometry"]["lng"]

        gmap = folium.Map(location=[lat,ing],zoom_start = 9)
        folium.Maker([lat,ing],popup=negara).add_to(gmap)
        gmap.save("index.html")

        print("==========================================")
        print("Internasional numbers:", internasional)
        print("Operator:", operator if operator else "Tidak Diketahui")
        print("Country:",negara)
        print("location:", lat,lng)
        print("==========================================")
        print()


    except phonenumbers.NumberParseException:
        print("Nomer Salah")
            
while True:
    if __name__ == "__main__":
        no = input("Masukan No Target: ")
        target(no)

        if no == "exit":
            break
