from manim import *
import numpy as np

from manim import *
import numpy as np
import math

class MLPaperExplanation(Scene):
    def construct(self):
        # Título principal con animación
        title = Text("Aplicación de Técnicas Avanzadas de Machine Learning", font_size=44, color=BLUE)
        subtitle = Text("Comparación NAS-SGD para Forecasting de Acciones", font_size=32, color=WHITE)
        subtitle2 = Text("Microsoft y Empresas Afiliadas", font_size=28, color=GRAY)
        author = Text("Jimena Yéssica Paricela Yana - UNAP", font_size=24, color=YELLOW)
        date = Text("14 de julio de 2025", font_size=20, color=GRAY)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN, buff=0.4)
        subtitle2.next_to(subtitle, DOWN, buff=0.3)
        author.next_to(subtitle2, DOWN, buff=0.5)
        date.next_to(author, DOWN, buff=0.3)
        
        # Animación de entrada
        self.play(Write(title))
        self.play(Write(subtitle))
        self.play(Write(subtitle2))
        self.play(Write(author))
        self.play(Write(date))
        
        # Agregar elementos decorativos
        decorative_line = Line(LEFT*6, RIGHT*6, color=BLUE, stroke_width=2)
        decorative_line.next_to(date, DOWN, buff=0.5)
        self.play(Create(decorative_line))
        
        self.wait(3)
        self.play(FadeOut(title, subtitle, subtitle2, author, date, decorative_line))

class IntroduccionProblema(Scene):
    def construct(self):
        # Título con animación
        problem_title = Text("El Desafío del Mercado Bursátil", font_size=42, color=YELLOW)
        problem_title.to_edge(UP)
        
        # Subtítulo explicativo
        subtitle = Text("Sistema complejo más dinámico para predicción computacional", font_size=24, color=GRAY)
        subtitle.next_to(problem_title, DOWN, buff=0.3)
        
        # Características del mercado con iconos
        caracteristicas = VGroup(
            VGroup( Text("Alta volatilidad", font_size=26)).arrange(RIGHT, buff=0.3),
            VGroup(Text( "Dependencias no lineales", font_size=26)).arrange(RIGHT, buff=0.3),
            VGroup(Text("Múltiples factores (económicos, políticos, sociales)", font_size=26)).arrange(RIGHT, buff=0.3),
            VGroup(Text("Patrones temporales complejos", font_size=26)).arrange(RIGHT, buff=0.3),
            VGroup(Text("Clustering de volatilidad", font_size=26)).arrange(RIGHT, buff=0.3)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Gráfico de volatilidad mejorado
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=5,
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": range(0, 11, 2)},
            y_axis_config={"numbers_to_include": range(-3, 4, 1)}
        )
        
        # Etiquetas de ejes
        x_label = Text("Tiempo (años)", font_size=20, color=WHITE)
        x_label.next_to(axes, DOWN, buff=0.5)
        y_label = Text("Volatilidad", font_size=20, color=WHITE)
        y_label.rotate(PI/2).next_to(axes, LEFT, buff=0.5)
        
        # Datos simulados más realistas
        np.random.seed(42)
        t = np.linspace(0, 10, 200)
        volatility_data = []
        for x in t:
            # Simular crisis financieras y períodos de estabilidad
            base_volatility = 0.5 * np.sin(0.5*x) + 0.3 * np.sin(2*x)
            # Crisis dot-com (alrededor de x=2)
            crisis_2000 = 2 * np.exp(-((x-2)**2)/0.5) if abs(x-2) < 2 else 0
            # Crisis 2008 (alrededor de x=6)
            crisis_2008 = 2.5 * np.exp(-((x-6)**2)/0.8) if abs(x-6) < 2 else 0
            # Ruido
            noise = 0.2 * np.random.randn()
            volatility_data.append(base_volatility + crisis_2000 + crisis_2008 + noise)
        
        volatility_graph = axes.plot_line_graph(
            x_values=t,
            y_values=volatility_data,
            line_color=RED,
            stroke_width=3
        )
        
        # Marcar crisis importantes
        crisis_2000_dot = Dot(axes.c2p(2, 2), color=ORANGE, radius=0.1)
        crisis_2008_dot = Dot(axes.c2p(6, 2.5), color=ORANGE, radius=0.1)
        crisis_2000_label = Text("Crisis dot-com\n(2000)", font_size=16, color=ORANGE)
        crisis_2008_label = Text("Crisis financiera\n(2008)", font_size=16, color=ORANGE)
        
        crisis_2000_label.next_to(crisis_2000_dot, UP, buff=0.3)
        crisis_2008_label.next_to(crisis_2008_dot, UP, buff=0.3)
        
        self.play(Write(problem_title))
        self.play(Write(subtitle))
        self.wait(1)
        
        for caracteristica in caracteristicas:
            self.play(Write(caracteristica))
            self.wait(0.5)
        
        self.wait(2)
        self.play(FadeOut(caracteristicas))
        
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.play(Write(x_label), Write(y_label))
        self.play(Create(volatility_graph))
        self.play(Create(crisis_2000_dot), Create(crisis_2008_dot))
        self.play(Write(crisis_2000_label), Write(crisis_2008_label))
        
        self.wait(3)
        self.play(FadeOut(problem_title, subtitle, axes, x_label, y_label, volatility_graph, 
                          crisis_2000_dot, crisis_2008_dot, crisis_2000_label, crisis_2008_label))

class DatasetDetailedInfo(Scene):
    def construct(self):
        title = Text("Dataset Utilizado - Información Detallada", font_size=40, color=BLUE)
        title.to_edge(UP)
        
        # Información principal de Microsoft
        msft_info = VGroup(
            Text("Microsoft Corporation (NASDAQ: MSFT)", font_size=32, color=YELLOW),
            Text("Fundada: 1975 | Cotizando desde: 1986", font_size=24, color=GRAY),
            Text("Período análisis: 13 marzo 1986 - 31 diciembre 2024", font_size=24),
            Text("Total: 38+ años de datos históricos", font_size=24),
            Text("Observaciones MSFT: 9,737 puntos de datos", font_size=24, color=GREEN)
        ).arrange(DOWN, buff=0.3)
        
        # Crear tabla de acciones
        table_title = Text("Empresas Afiliadas Analizadas", font_size=28, color=GREEN)
        
        # Datos de las acciones del paper
        stock_data = [
            ["Acción", "Empresa", "Observaciones", "Sector"],
            ["DELL", "Dell Technologies", "2,065", "Tecnología"],
            ["IBM", "International Business Machines", "11,064", "Tecnología"],
            ["INTC", "Intel Corporation", "11,064", "Semiconductores"],
            ["MSFT", "Microsoft Corporation", "9,737", "Software"],
            ["SONY", "Sony Corporation", "11,064", "Electrónicos"],
            ["VZ", "Verizon Communications", "10,319", "Telecomunicaciones"]
        ]
        
        # Crear tabla visual
        table = VGroup()
        for i, row in enumerate(stock_data):
            table_row = VGroup()
            for j, cell in enumerate(row):
                if i == 0:  # Header
                    cell_text = Text(cell, font_size=20, color=YELLOW)
                else:
                    cell_text = Text(cell, font_size=18, color=WHITE)
                
                cell_rect = Rectangle(width=2.5, height=0.5, color=BLUE, fill_opacity=0.1)
                cell_text.move_to(cell_rect.get_center())
                table_row.add(VGroup(cell_rect, cell_text))
            
            table_row.arrange(RIGHT, buff=0)
            table.add(table_row)
        
        table.arrange(DOWN, buff=0)
        
        # Estadísticas adicionales
        stats = VGroup(
            Text("Total de observaciones: 55,313", font_size=24, color=BLUE),
            Text("Sectores representados: 4", font_size=24, color=BLUE),
            Text("Período total: 1986-2024", font_size=24, color=BLUE),
            Text("Capitalización promedio: $2.8T", font_size=24, color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        msft_info.shift(UP * 2)
        table_title.next_to(msft_info, DOWN, buff=0.8)
        table.next_to(table_title, DOWN, buff=0.5)
        stats.next_to(table, DOWN, buff=0.8)
        
        self.play(Write(title))
        self.play(Write(msft_info))
        self.wait(2)
        self.play(Write(table_title))
        
        # Animar tabla fila por fila
        for row in table:
            self.play(Create(row))
            self.wait(0.3)
        
        self.wait(2)
        self.play(Write(stats))
        self.wait(3)
        self.play(FadeOut(title, msft_info, table_title, table, stats))

class MetodosComparacionDetallada(Scene):
    def construct(self):
        title = Text("Métodos Comparados - Análisis Detallado", font_size=40, color=BLUE)
        title.to_edge(UP)
        
        # Crear dos columnas más detalladas
        sgd_box = RoundedRectangle(
            width=6, height=7, corner_radius=0.3, color=GREEN, fill_opacity=0.1
        ).shift(LEFT * 3.5)
        
        nas_box = RoundedRectangle(
            width=6, height=7, corner_radius=0.3, color=ORANGE, fill_opacity=0.1
        ).shift(RIGHT * 3.5)
        
        # Títulos mejorados
        sgd_title = Text("SGD con Momentum", font_size=28, color=GREEN, weight=BOLD)
        sgd_title.next_to(sgd_box, UP, buff=0.3)
        
        nas_title = Text("NAS-DARTS", font_size=28, color=ORANGE, weight=BOLD)
        nas_subtitle = Text("Differentiable Architecture Search", font_size=20, color=GRAY)
        nas_title.next_to(nas_box, UP, buff=0.3)
        nas_subtitle.next_to(nas_title, DOWN, buff=0.1)
        
        # Características SGD más detalladas
        sgd_features = VGroup(
            Text("Método tradicional probado", font_size=16, color=WHITE),
            Text("Arquitectura fija predefinida", font_size=16, color=WHITE),
            Text("Entrenamiento rápido", font_size=16, color=WHITE),
            Text("Menor complejidad computacional", font_size=16, color=WHITE),
            Text("Actualización: θ = θ - αvₜ", font_size=16, color=GRAY),
            Text("Tiempo promedio: 10.56s", font_size=16, color=GREEN),
            Text("Memoria eficiente", font_size=16, color=WHITE),
            Text("Convergencia predecible", font_size=16, color=WHITE),
            Text("Gana en 1/6 acciones", font_size=16, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        sgd_features.move_to(sgd_box)
        
        # Características NAS-DARTS más detalladas
        nas_features = VGroup(
            Text("Búsqueda automática de arquitecturas", font_size=16, color=WHITE),
            Text("Optimización continua y adaptativa", font_size=16, color=WHITE),
            Text("Mayor precisión predictiva", font_size=16, color=WHITE),
            Text("Mejora MAE: 19.2%", font_size=16, color=GREEN),
            Text("Mejora RMSE: 18.6%", font_size=16, color=GREEN),
            Text("Mejora MAPE: 23.0%", font_size=16, color=GREEN),
            Text("Tiempo promedio: 15.75s", font_size=16, color=ORANGE),
            Text("Gana en 5/6 acciones", font_size=16, color=GREEN),
            Text("Arquitectura adaptativa", font_size=16, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        nas_features.move_to(nas_box)
        
        # Fórmulas matemáticas
        sgd_formula = MathTex(r"\theta_{t+1} = \theta_t - \eta v_t", font_size=24, color=GREEN)
        sgd_formula.next_to(sgd_box, DOWN, buff=0.3)
        
        nas_formula = MathTex(r"o^{(i,j)} = \sum_{k \in O} \frac{\exp(\alpha_k^{(i,j)})}{\sum_{l \in O} \exp(\alpha_l^{(i,j)})} \cdot op_k(x^{(i)})", font_size=20, color=ORANGE)
        nas_formula.next_to(nas_box, DOWN, buff=0.3)
        
        self.play(Write(title))
        self.play(Create(sgd_box), Create(nas_box))
        self.play(Write(sgd_title), Write(nas_title), Write(nas_subtitle))
        
        # Animar características una por una
        for sgd_feat, nas_feat in zip(sgd_features, nas_features):
            self.play(Write(sgd_feat), Write(nas_feat))
            self.wait(0.3)
        
        self.play(Write(sgd_formula), Write(nas_formula))
        self.wait(3)
        self.play(FadeOut(title, sgd_box, nas_box, sgd_title, nas_title, nas_subtitle, 
                          sgd_features, nas_features, sgd_formula, nas_formula))

class ResultadosComparacionDetallada(Scene):
    def construct(self):
        title = Text("Resultados Experimentales Detallados", font_size=40, color=BLUE)
        title.to_edge(UP)
        
        # Crear gráfico de barras múltiples para todas las métricas
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 0.08, 0.01],
            x_length=12,
            y_length=6,
            axis_config={"color": BLUE},
            y_axis_config={"decimal_number_config": {"num_decimal_places": 3}}
        )
        
        # Datos del paper
        stocks = ["DELL", "IBM", "INTC", "MSFT", "SONY", "VZ"]
        sgd_mae = [0.0631, 0.0334, 0.0326, 0.0249, 0.0471, 0.0364]
        nas_mae = [0.0445, 0.0295, 0.0390, 0.0204, 0.0272, 0.0315]
        sgd_rmse = [0.0969, 0.0455, 0.0484, 0.0404, 0.0683, 0.0513]
        nas_rmse = [0.0691, 0.0409, 0.0509, 0.0326, 0.0464, 0.0456]
        
        # Crear barras agrupadas
        bars_sgd_mae = VGroup()
        bars_nas_mae = VGroup()
        bars_sgd_rmse = VGroup()
        bars_nas_rmse = VGroup()
        
        bar_width = 0.15
        for i, stock in enumerate(stocks):
            x_pos = i + 1
            
            # Barras MAE
            bar_sgd_mae = Rectangle(
                width=bar_width,
                height=sgd_mae[i] * 75,
                color=GREEN,
                fill_opacity=0.7
            ).move_to(axes.c2p(x_pos - 0.225, sgd_mae[i]/2))
            
            bar_nas_mae = Rectangle(
                width=bar_width,
                height=nas_mae[i] * 75,
                color=ORANGE,
                fill_opacity=0.7
            ).move_to(axes.c2p(x_pos - 0.075, nas_mae[i]/2))
            
            # Barras RMSE
            bar_sgd_rmse = Rectangle(
                width=bar_width,
                height=sgd_rmse[i] * 75,
                color=RED,
                fill_opacity=0.5
            ).move_to(axes.c2p(x_pos + 0.075, sgd_rmse[i]/2))
            
            bar_nas_rmse = Rectangle(
                width=bar_width,
                height=nas_rmse[i] * 75,
                color=PURPLE,
                fill_opacity=0.5
            ).move_to(axes.c2p(x_pos + 0.225, nas_rmse[i]/2))
            
            bars_sgd_mae.add(bar_sgd_mae)
            bars_nas_mae.add(bar_nas_mae)
            bars_sgd_rmse.add(bar_sgd_rmse)
            bars_nas_rmse.add(bar_nas_rmse)
        
        # Etiquetas de acciones
        stock_labels = VGroup()
        for i, stock in enumerate(stocks):
            label = Text(stock, font_size=16, color=WHITE)
            label.next_to(axes.c2p(i + 1, 0), DOWN, buff=0.3)
            stock_labels.add(label)
        
        # Leyenda mejorada
        legend = VGroup(
            VGroup(
                Rectangle(width=0.3, height=0.2, color=GREEN, fill_opacity=0.7),
                Text("SGD MAE", font_size=16, color=WHITE)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Rectangle(width=0.3, height=0.2, color=ORANGE, fill_opacity=0.7),
                Text("DARTS MAE", font_size=16, color=WHITE)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Rectangle(width=0.3, height=0.2, color=RED, fill_opacity=0.5),
                Text("SGD RMSE", font_size=16, color=WHITE)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Rectangle(width=0.3, height=0.2, color=PURPLE, fill_opacity=0.5),
                Text("DARTS RMSE", font_size=16, color=WHITE)
            ).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, buff=0.2)
        legend.to_corner(UR)
        
        # Etiquetas de ejes
        y_label = Text("Error", font_size=20, color=WHITE)
        y_label.rotate(PI/2).next_to(axes, LEFT, buff=0.5)
        
        x_label = Text("Acciones", font_size=20, color=WHITE)
        x_label.next_to(axes, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Create(axes))
        self.play(Write(y_label), Write(x_label))
        self.play(Write(stock_labels))
        self.play(Write(legend))
        
        # Animar barras por grupos
        self.play(Create(bars_sgd_mae))
        self.wait(0.5)
        self.play(Create(bars_nas_mae))
        self.wait(0.5)
        self.play(Create(bars_sgd_rmse))
        self.wait(0.5)
        self.play(Create(bars_nas_rmse))
        
        self.wait(3)
        self.play(FadeOut(title, axes, y_label, x_label, stock_labels, legend,
                          bars_sgd_mae, bars_nas_mae, bars_sgd_rmse, bars_nas_rmse))

class MAPEComparison(Scene):
    def construct(self):
        title = Text("Análisis MAPE (Error Porcentual Absoluto Medio)", font_size=36, color=BLUE)
        title.to_edge(UP)
        
        # Datos MAPE del paper
        stocks = ["DELL", "IBM", "INTC", "MSFT", "SONY", "VZ"]
        sgd_mape = [60.01, 36.47, 36.09, 5.25, 23.53, 20.42]
        nas_mape = [47.31, 28.70, 23.52, 4.45, 20.43, 15.61]
        
        # Crear gráfico de barras horizontales
        axes = Axes(
            x_range=[0, 70, 10],
            y_range=[0, 7, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE}
        )
        
        # Crear barras horizontales
        bars_sgd = VGroup()
        bars_nas = VGroup()
        
        for i, (stock, sgd_val, nas_val) in enumerate(zip(stocks, sgd_mape, nas_mape)):
            y_pos = i + 1
            
            # SGD bars
            bar_sgd = Rectangle(
                width=sgd_val * 0.14,
                height=0.3,
                color=GREEN,
                fill_opacity=0.7
            ).move_to(axes.c2p(sgd_val/2, y_pos - 0.2))
            
            # NAS bars
            bar_nas = Rectangle(
                width=nas_val * 0.14,
                height=0.3,
                color=ORANGE,
                fill_opacity=0.7
            ).move_to(axes.c2p(nas_val/2, y_pos + 0.2))
            
            bars_sgd.add(bar_sgd)
            bars_nas.add(bar_nas)
            
            # Etiquetas de valores
            sgd_label = Text(f"{sgd_val:.1f}%", font_size=14, color=WHITE)
            sgd_label.next_to(bar_sgd, RIGHT, buff=0.1)
            
            nas_label = Text(f"{nas_val:.1f}%", font_size=14, color=WHITE)
            nas_label.next_to(bar_nas, RIGHT, buff=0.1)
            
            bars_sgd.add(sgd_label)
            bars_nas.add(nas_label)
        
        # Etiquetas de acciones
        stock_labels = VGroup()
        for i, stock in enumerate(stocks):
            label = Text(stock, font_size=18, color=WHITE)
            label.next_to(axes.c2p(0, i + 1), LEFT, buff=0.5)
            stock_labels.add(label)
        
        # Etiquetas de ejes
        x_label = Text("MAPE (%)", font_size=20, color=WHITE)
        x_label.next_to(axes, DOWN, buff=0.5)
        
        # Leyenda
        legend = VGroup(
            VGroup(
                Rectangle(width=0.3, height=0.2, color=GREEN, fill_opacity=0.7),
                Text("SGD", font_size=18, color=WHITE)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Rectangle(width=0.3, height=0.2, color=ORANGE, fill_opacity=0.7),
                Text("NAS-DARTS", font_size=18, color=WHITE)
            ).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, buff=0.3)
        legend.to_corner(UR)
        
        self.play(Write(title))
        self.play(Create(axes))
        self.play(Write(x_label))
        self.play(Write(stock_labels))
        self.play(Write(legend))
        
        # Animar barras
        for bar_sgd, bar_nas in zip(bars_sgd, bars_nas):
            self.play(Create(bar_sgd), Create(bar_nas))
            self.wait(0.2)
        
        self.wait(3)
        self.play(FadeOut(title, axes, x_label, stock_labels, legend, bars_sgd, bars_nas))


class MejorasyBeneficios(Scene):
    def construct(self):
        title = Text("Mejoras de NAS-DARTS", font_size=48, color=ORANGE)
        title.to_edge(UP)
        
        # Crear métricas de mejora
        mejoras = VGroup(
            Text("MAE: 19.2% de mejora", font_size=32, color=GREEN),
            Text("RMSE: 18.6% de mejora", font_size=32, color=GREEN),
            Text("MAPE: 23.0% de mejora", font_size=32, color=GREEN)
        ).arrange(DOWN, buff=0.5)
        
        # Crear círculos de progreso animados
        circles = VGroup()
        percentages = [19.2, 18.6, 23.0]
        
        for i, (mejora, percent) in enumerate(zip(mejoras, percentages)):
            circle = Circle(radius=0.8, color=BLUE)
            circle.move_to(mejora.get_center() + RIGHT * 4)
            
            # Arco de progreso
            arc = Arc(
                radius=0.8,
                start_angle=PI/2,
                angle=-2*PI*(percent/100),
                color=GREEN,
                stroke_width=8
            )
            arc.move_to(circle.get_center())
            
            # Texto del porcentaje
            percent_text = Text(f"{percent}%", font_size=24, color=WHITE)
            percent_text.move_to(circle.get_center())
            
            circles.add(VGroup(circle, arc, percent_text))
        
        self.play(Write(title))
        self.play(Write(mejoras))
        
        for i, circle_group in enumerate(circles):
            self.play(Create(circle_group[0]))  # Círculo base
            self.play(Create(circle_group[1]))  # Arco de progreso
            self.play(Write(circle_group[2]))   # Texto del porcentaje
            self.wait(0.5)
        
        self.wait(2)
        self.play(FadeOut(title, mejoras, circles))

class Conclusiones(Scene):
    def construct(self):
        title = Text("Conclusiones", font_size=48, color=BLUE)
        title.to_edge(UP)
        
        # Conclusiones principales
        conclusiones = VGroup(
            Text("1. NAS-DARTS supera a SGD en precisión predictiva", font_size=24),
            Text("2. SGD mantiene ventaja en eficiencia computacional", font_size=24),
            Text("3. La elección depende del balance precisión vs velocidad", font_size=24),
            Text("4. NAS-DARTS es ideal para aplicaciones críticas", font_size=24),
            Text("5. Ambos métodos muestran potencial para finanzas", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Recomendación final
        recomendacion = VGroup(
            Text("Recomendación:", font_size=32, color=YELLOW),
            Text("• Precisión crítica → NAS-DARTS", font_size=24),
            Text("• Tiempo real → SGD", font_size=24),
            Text("• Híbrido → Combinar ambos enfoques", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        conclusiones.shift(UP * 1)
        recomendacion.shift(DOWN * 1.5)
        
        self.play(Write(title))
        
        for conclusion in conclusiones:
            self.play(Write(conclusion))
            self.wait(0.5)
        
        self.wait(1)
        self.play(Write(recomendacion))
        self.wait(3)
        
        # Fade out final
        self.play(FadeOut(title, conclusiones, recomendacion))

class DatasetInfo(Scene):
    def construct(self):
        title = Text("Dataset Utilizado", font_size=48, color=BLUE)
        title.to_edge(UP)
        
        # Información del dataset
        dataset_info = VGroup(
            Text("Microsoft Corporation (NASDAQ: MSFT)", font_size=32, color=YELLOW),
            Text("Período: 13 marzo 1986 - 31 diciembre 2024", font_size=24),
            Text("Total: 38+ años de datos históricos", font_size=24),
            Text("Observaciones: 9,737 puntos de datos", font_size=24)
        ).arrange(DOWN, buff=0.5)
        
        # Otras acciones incluidas
        other_stocks = VGroup(
            Text("Otras acciones analizadas:", font_size=28, color=GREEN),
            Text("• DELL: 2,065 observaciones", font_size=22),
            Text("• IBM: 11,064 observaciones", font_size=22),
            Text("• INTC: 11,064 observaciones", font_size=22),
            Text("• SONY: 11,064 observaciones", font_size=22),
            Text("• VZ: 10,319 observaciones", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        dataset_info.shift(UP * 1)
        other_stocks.shift(DOWN * 1.5)
        
        self.play(Write(title))
        self.play(Write(dataset_info))
        self.wait(2)
        self.play(Write(other_stocks))
        self.wait(3)
        self.play(FadeOut(title, dataset_info, other_stocks))

# Escena principal que ejecuta todas las secciones
class PaperCompleto(Scene):
    def construct(self):
        scenes = [
            MLPaperExplanation(),
            IntroduccionProblema(),
            DatasetDetailedInfo(),
            MetodosComparacionDetallada(),
            ResultadosComparacionDetallada(),
            MAPEComparison(),
            MejorasyBeneficios(),
            Conclusiones()
        ]
        
        for scene in scenes:
            scene.construct()
            self.wait(1) 