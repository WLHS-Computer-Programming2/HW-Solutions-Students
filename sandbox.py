import cmath
import matplotlib.pyplot as plt

def get_complex_input():
    real = float(input("Enter the real part of the complex number: "))
    imag = float(input("Enter the imaginary part of the complex number: "))
    return complex(real, imag)

def illustrate_demoivre(z, n):
    r, theta = cmath.polar(z)
    print(f"\nOriginal complex number: {z}")
    print(f"Polar form: r = {r:.4f}, θ = {theta:.4f} radians")

    powers = []
    print("\nPowers using DeMoivre's Theorem:")
    for k in range(1, n + 1):
        rk = r**k
        thetak = theta * k
        zk = cmath.rect(rk, thetak)
        powers.append(zk)
        print(f"{k}) z^{k} = {zk:.4f} (Polar: r^{k} = {rk:.4f}, θ·{k} = {thetak:.4f})")

    return powers

def plot_powers(powers):
    plt.figure(figsize=(6, 6))
    for i, z in enumerate(powers, start=1):
        # Draw a line from origin to the point
        plt.plot([0, z.real], [0, z.imag], linestyle='--', linewidth=1)
        # Plot the point
        plt.plot(z.real, z.imag, 'o', label=f'z^{i}')
        # Label the point
        plt.text(z.real, z.imag, f'{i}', fontsize=12, ha='center', va='bottom')

    plt.axhline(0, color='gray', lw=0.5)
    plt.axvline(0, color='gray', lw=0.5)
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.title("Powers of a Complex Number (DeMoivre's Theorem)")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()


# Main script
if __name__ == "__main__":
    z = get_complex_input()
    n = int(input("Enter the highest power to compute: "))
    powers = illustrate_demoivre(z, n)
    
    plot = input("\nWould you like to plot the powers on the complex plane? (y/n): ").lower()
    if plot == 'y':
        plot_powers(powers)
