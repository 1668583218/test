from pyecharts.charts import Bar, Pie
from pyecharts import options as opts
from pyecharts.faker import Faker


def pie_base() -> Pie:
    c = (
        Pie()
            .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
            .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c


pie_base().render(path="bingtu.html")

