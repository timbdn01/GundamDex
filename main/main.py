from gundam import Gundam

def main():
    # Create an instance of Gundam
    gundam1 = Gundam(
        name="Gundam",
        model_number="RX-78-2",
        pilot="Amuro Ray",
        weapons=["Beam Rifle", "Beam Saber", "Shield"],
        series="Mobile Suit Gundam",
        status="Destroyed",
        height=18.0,
        weight=60.0,
        gunpla_available=True,
        gunpla_grades=["High Grade", "Real Grade", "Master Grade", "Perfect Grade"]
    )

    gundam2 = Gundam(
        name="Freedom Gundam",
        model_number="ZGMF-X10A",
        pilot="Kira Yamato",
        weapons=["Beam Rifle", "Beam Sabers", "Plasma Beam Cannons"],
        series="Mobile Suit Gundam SEED",
        status="Destroyed",
        height=17.3,
        weight=58.0,
        gunpla_available=True,
        gunpla_grades=["High Grade", "Real Grade", "Master Grade", "Perfect Grade"]
    )

    # Display information about the Gundams
    print(gundam1.display_info())
    print(gundam2.display_info())