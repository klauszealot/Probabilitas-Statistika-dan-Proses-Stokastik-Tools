import tkinter as tk
from tkinter import ttk, messagebox
import math
import scipy.stats as stats
import numpy as np

class StatsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Probabilitas, Statistika, dan Proses Stokastik Tool")
        self.root.geometry("900x750")
        
        # Style
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Calibri", 10))
        self.style.configure("TButton", font=("Calibri", 10))
        self.style.configure("Header.TLabel", font=("Calibri", 12, "bold"))
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        self.setup_prob_comb_tab()
        self.setup_distributions_tab()
        self.setup_sampling_tab()
        self.setup_hypothesis_tab()
        self.setup_anova_tab()

    def create_scrollable_tab(self, text):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=text)
        
        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Enable mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        return scrollable_frame

    def create_section(self, parent, title, inputs, calc_func):
        frame = ttk.LabelFrame(parent, text=title)
        frame.pack(fill="x", padx=10, pady=5)
        
        entries = {}
        for i, (key, label) in enumerate(inputs.items()):
            ttk.Label(frame, text=label).grid(row=0, column=i*2, padx=5, pady=5)
            entry = ttk.Entry(frame, width=10)
            entry.grid(row=0, column=i*2+1, padx=5, pady=5)
            entries[key] = entry
            
        result_label = ttk.Label(frame, text="Hasil: -", font=("Calibri", 10, "bold"), foreground="blue")
        result_label.grid(row=0, column=len(inputs)*2 + 1, padx=10, pady=5)
        
        def on_calc(event=None):
            try:
                data = {k: float(e.get()) for k, e in entries.items()}
                res = calc_func(data)
                if isinstance(res, float):
                    result_label.config(text=f"Hasil: {res:.4f}")
                else:
                    result_label.config(text=f"Hasil: {res}")
            except Exception as e:
                messagebox.showerror("Error", f"Input tidak valid: {e}")
        
        btn = ttk.Button(frame, text="Hitung", command=on_calc)
        btn.grid(row=0, column=len(inputs)*2, padx=5, pady=5)
        
        # Bind Enter key to all entries in this section
        for entry in entries.values():
            entry.bind("<Return>", on_calc)

    def setup_prob_comb_tab(self):
        parent = self.create_scrollable_tab("Prob & Komb")
        
        self.create_section(parent, "Peluang Suatu Kejadian P(A) = n/N", 
                           {"n": "n:", "N": "N:"}, 
                           lambda d: d['n'] / d['N'])
        
        self.create_section(parent, "Aturan Penjumlahan (Saling Lepas)", 
                           {"pa": "P(A):", "pb": "P(B):"}, 
                           lambda d: d['pa'] + d['pb'])
        
        self.create_section(parent, "Aturan Penjumlahan (Sembarang)", 
                           {"pa": "P(A):", "pb": "P(B):", "pab": "P(A ∩ B):"}, 
                           lambda d: d['pa'] + d['pb'] - d['pab'])
        
        self.create_section(parent, "Probabilitas Bersyarat P(B|A)", 
                           {"pab": "P(A ∩ B):", "pa": "P(A):"}, 
                           lambda d: d['pab'] / d['pa'])
        
        self.create_section(parent, "Kejadian Saling Bebas P(A ∩ B)", 
                           {"pa": "P(A):", "pb": "P(B):"}, 
                           lambda d: d['pa'] * d['pb'])

        self.create_section(parent, "Teorema Bayes (2 Kejadian: B1, B2)", 
                           {"pb1": "P(B1):", "pab1": "P(A|B1):", "pb2": "P(B2):", "pab2": "P(A|B2):"}, 
                           lambda d: (d['pb1']*d['pab1']) / (d['pb1']*d['pab1'] + d['pb2']*d['pab2']))
        
        self.create_section(parent, "Permutasi nP r", 
                           {"n": "n:", "r": "r:"}, 
                           lambda d: math.perm(int(d['n']), int(d['r'])))
        
        self.create_section(parent, "Kombinasi nC r", 
                           {"n": "n:", "r": "r:"}, 
                           lambda d: math.comb(int(d['n']), int(d['r'])))

        self.create_section(parent, "Nilai Harapan E(X) [Contoh 2 titik]", 
                           {"x1": "x1:", "fx1": "f(x1):", "x2": "x2:", "fx2": "f(x2):"}, 
                           lambda d: d['x1']*d['fx1'] + d['x2']*d['fx2'])

        self.create_section(parent, "Varians σ² [Contoh 2 titik]", 
                           {"x1": "x1:", "fx1": "f(x1):", "x2": "x2:", "fx2": "f(x2):", "mu": "μ:"}, 
                           lambda d: (d['x1']-d['mu'])**2 * d['fx1'] + (d['x2']-d['mu'])**2 * d['fx2'])

    def setup_distributions_tab(self):
        parent = self.create_scrollable_tab("Distribusi")
        
        self.create_section(parent, "Distribusi Binomial b(x; n, p)", 
                           {"x": "x:", "n": "n:", "p": "p:"}, 
                           lambda d: stats.binom.pmf(int(d['x']), int(d['n']), d['p']))
        
        self.create_section(parent, "Rata-rata & Varians Binomial", 
                           {"n": "n:", "p": "p:"}, 
                           lambda d: f"μ={d['n']*d['p']:.2f}, σ²={d['n']*d['p']*(1-d['p']):.2f}")
        
        self.create_section(parent, "Distribusi Poisson p(x; μ)", 
                           {"x": "x:", "mu": "μ:"}, 
                           lambda d: stats.poisson.pmf(int(d['x']), d['mu']))
        
        self.create_section(parent, "Fungsi Densitas Normal f(x; μ, σ)", 
                           {"x": "x:", "mu": "μ:", "sigma": "σ:"}, 
                           lambda d: stats.norm.pdf(d['x'], d['mu'], d['sigma']))

        self.create_section(parent, "Transformasi Normal Baku (Nilai Z)", 
                           {"x": "X:", "mu": "μ:", "sigma": "σ:"}, 
                           lambda d: (d['x'] - d['mu']) / d['sigma'])

    def setup_sampling_tab(self):
        parent = self.create_scrollable_tab("Sampling")
        
        self.create_section(parent, "SE Rata-rata (Populasi Tak Terbatas)", 
                           {"sigma": "σ:", "n": "n:"}, 
                           lambda d: d['sigma'] / math.sqrt(d['n']))
        
        self.create_section(parent, "SE Rata-rata (Populasi Terbatas)", 
                           {"sigma": "σ:", "n": "n:", "N": "N:"}, 
                           lambda d: (d['sigma'] / math.sqrt(d['n'])) * math.sqrt((d['N']-d['n'])/(d['N']-1)))
        
        self.create_section(parent, "SE Proporsi (Populasi Tak Terbatas)", 
                           {"p": "p:", "n": "n:"}, 
                           lambda d: math.sqrt((d['p']*(1-d['p']))/d['n']))
        
        self.create_section(parent, "SE Proporsi (Populasi Terbatas)", 
                           {"p": "p:", "n": "n:", "N": "N:"}, 
                           lambda d: math.sqrt((d['p']*(1-d['p']))/d['n']) * math.sqrt((d['N']-d['n'])/(d['N']-1)))

    def setup_hypothesis_tab(self):
        parent = self.create_scrollable_tab("Hipotesis")
        
        self.create_section(parent, "Estimasi Rata-rata (Sampel Besar n ≥ 30)", 
                           {"xbar": "X̄:", "z": "Zα/2:", "sigma": "σ:", "n": "n:"}, 
                           lambda d: f"{d['xbar'] - d['z']*(d['sigma']/math.sqrt(d['n'])):.4f} < μ < {d['xbar'] + d['z']*(d['sigma']/math.sqrt(d['n'])):.4f}")
        
        self.create_section(parent, "Estimasi Rata-rata (Sampel Kecil n < 30)", 
                           {"xbar": "x̄:", "t": "tα/2:", "s": "s:", "n": "n:"}, 
                           lambda d: f"{d['xbar'] - d['t']*(d['s']/math.sqrt(d['n'])):.4f} < μ < {d['xbar'] + d['t']*(d['s']/math.sqrt(d['n'])):.4f}")

        self.create_section(parent, "Estimasi Proporsi", 
                           {"phat": "p̂:", "z": "Zα/2:", "n": "n:"}, 
                           lambda d: f"{d['phat'] - d['z']*math.sqrt((d['phat']*(1-d['phat']))/d['n']):.4f} < p < {d['phat'] + d['z']*math.sqrt((d['phat']*(1-d['phat']))/d['n']):.4f}")

        self.create_section(parent, "Margin of Error Rata-rata", 
                           {"z": "Zα/2:", "sigma": "σ:", "n": "n:"}, 
                           lambda d: d['z'] * (d['sigma']/math.sqrt(d['n'])))

        self.create_section(parent, "Uji Z Satu Rata-rata (Sampel Besar)", 
                           {"xbar": "X̄:", "mu0": "μ0:", "sigma": "σ:", "n": "n:"}, 
                           lambda d: (d['xbar'] - d['mu0']) / (d['sigma']/math.sqrt(d['n'])))

        self.create_section(parent, "Uji t Satu Rata-rata (Sampel Kecil)", 
                           {"xbar": "X̄:", "mu0": "μ0:", "s": "s:", "n": "n:"}, 
                           lambda d: (d['xbar'] - d['mu0']) / (d['s']/math.sqrt(d['n'])))

        self.create_section(parent, "Uji Z Beda Dua Rata-rata (Sampel Besar)", 
                           {"xb1": "X̄1:", "xb2": "X̄2:", "s1": "σ1:", "n1": "n1:", "s2": "σ2:", "n2": "n2:"}, 
                           lambda d: (d['xb1'] - d['xb2']) / math.sqrt((d['s1']**2/d['n1']) + (d['s2']**2/d['n2'])))

        self.create_section(parent, "Uji Z Satu Proporsi", 
                           {"phat": "p̂:", "P": "P0:", "n": "n:"}, 
                           lambda d: (d['phat'] - d['P']) / math.sqrt((d['P']*(1-d['P']))/d['n']))

        self.create_section(parent, "Uji Z Beda Dua Proporsi", 
                           {"p1": "p̂1:", "p2": "p̂2:", "pg": "p̄:", "qg": "q̄:", "n1": "n1:", "n2": "n2:"}, 
                           lambda d: (d['p1'] - d['p2']) / math.sqrt(d['pg']*d['qg']*(1/d['n1'] + 1/d['n2'])))

    def setup_anova_tab(self):
        parent = self.create_scrollable_tab("ANOVA")
        
        self.create_section(parent, "ANOVA 1 Arah (Kalkulasi F)", 
                           {"jkp": "JKP:", "jke": "JKE:", "k": "k (perlakuan):", "N": "N (total):"}, 
                           lambda d: (d['jkp']/(d['k']-1)) / (d['jke']/(d['N']-d['k'])))

        self.create_section(parent, "ANOVA 2 Arah - F Perlakuan", 
                           {"jkp": "JKP:", "jke": "JKE:", "k": "k:", "b": "b:"}, 
                           lambda d: (d['jkp']/(d['k']-1)) / (d['jke']/((d['k']-1)*(d['b']-1))))
        
        self.create_section(parent, "ANOVA 2 Arah - F Blok", 
                           {"jkb": "JKB:", "jke": "JKE:", "k": "k:", "b": "b:"}, 
                           lambda d: (d['jkb']/(d['b']-1)) / (d['jke']/((d['k']-1)*(d['b']-1))))



if __name__ == "__main__":
    root = tk.Tk()
    app = StatsApp(root)
    root.mainloop()
