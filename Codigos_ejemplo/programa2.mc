int i;
bool bandera;
i = 0;
bandera = true;

while (i < 10 && bandera == true) {
    if (i == 5) {
        print 'Llegamos a la mitad';
    } else {
        print i;
    }
    i = i + 1;
}
