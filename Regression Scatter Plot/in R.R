library("ggplot2")

df_ad_expenditure <- read.csv("C:/Users/sbyeg/Downloads/scatter_plot_ii.csv",
                              header = TRUE,
                              sep = ",")

regression_scatter <- ggplot(df_ad_expenditure,
                             aes(x = Budget,
                                 y = Sales)) +
                      geom_point(size = 3,
