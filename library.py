
# Chegali method


def chegali(p: float, m: float, v: float):
    """
        متد محاسبه چگالی
    Args:
        p (float, optional): [چگالی]. Defaults to -1.
        m (float, optional): [جرم]. Defaults to -1.
        v (float, optional): [حجم]. Defaults to -1.

    Returns:
        [type]: [مقدار محاسبه شده را با توجه به ورودی بر می گرداند]
    """
    if p == -1:
        return m/v
    elif m == -1:
        return p*v
    else:
        return m/p

# khoon method


def khoon(antiA, antiB, antiD):
    """
     متد تایین گروه خونی
    Args:
        antiA (str, optional): [آنتی A]. Defaults to 0.
        antiB (str, optional): [آنتی B]. Defaults to 0.
        antiD (str, optional): [آنتی D]. Defaults to 0.
    Returns:
        [type]: [گروه خونی را با توجه به ورودی برمی گرداند]
    """
    if antiA == -1 and antiB == -1 and antiD == 1:
        print('O+')
    elif antiA == -1 and antiB == 1 and antiD == -1:
        print('B-')
    elif antiA == -1 and antiB == 1 and antiD == 1:
        print('B+')
    elif antiA == 1 and antiB == 1 and antiD == 1:
        print('AB+')
    elif antiA == 1 and antiB == 1 and antiD == -1:
        print('AB-')
    elif antiA == 1 and antiB == -1 and antiD == -1:
        print('A-')
    else:
        print('A+')

# takhmin_masafat method


def takhmin_masafat(meghias: float, f_map: float, f_ground: float):
    """
    متد محاسبه مقیاس

    Args:
        meghias (floatl,optional): [مقیاس] Defaults to -1 .
        f_map (float,optional): [فاصله دو نقطه روی نقشه] Defaults to -1 .
        f_ground (float,optional): [فاصله دو نقطه روی زمین] Defaults to -1 .
    Returns:
        [Type] : [مقیاس را با توجه به ورودی برمیگرداند]
    """
    if meghias == -1:
        return f_map/f_ground
    elif f_map == -1:
        return meghias * f_ground
    else:
        return f_map/meghias

# takhalkhol method


def cheshme(takhalkhol: float, v_sang: float, v_kol: float):
    """
    متد محاسبه تخلخل

    args:
        takhal (float,optional): [تخلخل] Defaults to -1.
        v_sang (float,optional): [حجم فضای خالی سنگ یا رسوب] Defaults to -1.
        v_kol (float,optional):  [حجم کل فضای سنگ یا رسوب] Defaults to -1.
    Returns : 
    [type] : [مقدار تخلخل را با توجه به ورودی برمی گرداند]

    """
    if takhalkhol == -1:
        return (v_sang/v_kol)*100
    elif v_sang == -1:
        return (takhalkhol*v_sang)/100
    else:
        return (v_sang/takhalkhol)*100