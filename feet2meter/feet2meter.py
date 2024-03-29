def feet2meter(v):
    feet = float(v[:-2])
    meters = feet * 0.3048
    return meters

def main():
    v = feet2meter(input("Сколько футов: "))
    print(f"Это будет {v:.3f} метров.")

main()
