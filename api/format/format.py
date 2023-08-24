from collections import OrderedDict


def prod_res(data):
    return OrderedDict({
        "id": data.id,
        'name':data.name,
        "prod_id":data.prod_id,
        "img":data.img.url,
        "color":data.color,
    })


def basketFormat(data):
    return OrderedDict({
        "product":data.product.product_id,
        "quantity":data.quantity,
    })


def productFormat(data):
    return OrderedDict({
        "product_id": data.product_id,
        "ctg": data.ctg.name,
        "style": data.style.name,
        "material": data.material,
        "color": data.color,
        "img": data.img.url,
    })


def format_cnt(data):
    return {
        "name": data.name,
        "phone": data.phone,
    }