s='Hi Bapu Guru Sathwik be with me please'
def rev(ss):
    return ss[::-1]
print(' '.join(map(rev,s.split()[::2])))

print(''.join(s[::2]))
print(''.join(s[1::2]))