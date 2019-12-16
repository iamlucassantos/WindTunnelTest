from typing import Dict, List
from numpy import array


def ingest_XFLR5(filename: str) -> Dict[str, List]:
    data = open(filename, 'r').readlines()[8:-2]

    def get_list(start, end):
        lst = [float(line[start:end]) for line in data]
        return lst

    alpha = get_list(0, 10)
    cl = get_list(10, 21)
    icd = array(get_list(21, 32))
    pcd = array(get_list(32, 43))
    cd = (icd + pcd) / 2
    tcd = get_list(42, 54)
    cm = get_list(65, 76)

    cleaned_data = {"alpha": alpha, "C_L": cl, "C_D": cd, "TCd": tcd, "C_m": cm}
    return cleaned_data


def ingest_experimental(filename: str) -> Dict[str, List]:
    data = open(filename, 'r').readlines()[2:]

    def get_list(start, end):
        lst = [float(line.replace('\t', "    ")[start:end]) for line in data]
        return lst

    alpha = get_list(11, 20)
    cl = get_list(36, 44)
    cd = get_list(44, 56)
    ct = get_list(84, 93)  # I assume that the torque coefficient is the same as the moment coefficient
    v = get_list(156, 165)
    re = get_list(165, 180)
    m = get_list(180, 188)

    cleaned_data = {'alpha': alpha, 'C_L': cl, 'C_D': cd, 'C_m': ct, 'v': v, 'Re': re, 'M': m}
    return cleaned_data


if __name__ == "__main__":
    ingest_experimental('3D_balance/corr_test.txt')
    ingest_XFLR5("XFLR5/finalRe735000-45m s.txt")
    print("test successful")
