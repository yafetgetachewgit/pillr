import scipy as sp
import matplotlib.pyplot as plt
import helpers

d = 10
data = sp.genfromtxt("data.dat", delimiter="\t")

x = data[:, 0]
y = data[:, 1]

plt.scatter(x, y, s=10)
plt.title("Desease Spread (Ebola)")
plt.xlabel("time")
plt.ylabel("detections")
plt.xticks([w*7*24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight = True)
plt.grid(True, linestyle="-", color='0.75')

# polynomial of degree 1 (straight line)
fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
f1 = sp.poly1d(fp1)

fx = sp.linspace(0, x[-1], 1000)
plt.plot(fx, f1(fx), linewidth=2)


#polynomial of degree n (curve)
f2p = sp.polyfit(x, y, d)
f2 = sp.poly1d(f2p)

plt.plot(fx, f2(fx), linewidth=2)


print(helpers.error(f2, x, y))


print("\n ======= \n The function:")
print(f2p)
print("of order : %i is the green curve"% d)

inflection = 3.5*7*24

print("\n\n\n There is an inflection point at %f hours" % inflection)

xa = x[:inflection]
ya = y[:inflection]
xb = x[inflection:]
yb = y[inflection:]

fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))

fa_error = helpers.error(fa, xa, ya)
fb_error = helpers.error(fb, xb, yb)

print("Error inflection=%f" % (fa_error + fb_error))
print("This error is the sum of lines red and cyan")

plt.plot(fx, fa(fx), linewidth=2)
plt.plot(fx, fb(fx), linewidth=2)





#show plot
plt.show()
