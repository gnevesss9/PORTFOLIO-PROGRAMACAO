"""Aplicação Flask para calcular a força de empuxo sobre um corpo."""

from flask import Flask, render_template, request

app = Flask(__name__)

# Aceleração gravitacional média (m/s²) utilizada no cálculo do empuxo.
ACELERACAO_GRAVITACIONAL = 9.81


@app.route("/", methods=["GET", "POST"])
def indice():
    """Mostra o formulário inicial e processa os dados submetidos pelo utilizador."""
    # Valores padrão quando a página é carregada pela primeira vez.
    forca = None
    estado = None

    if request.method == "POST":
        # Obtém os dados enviados pelo formulário, convertendo-os diretamente para float.
        densidade = request.form.get("densidade", type=float)
        volume = request.form.get("volume", type=float)

        # Prossegue com o cálculo apenas se ambos os valores forem fornecidos.
        if densidade is not None and volume is not None:
            forca = densidade * ACELERACAO_GRAVITACIONAL * volume
            estado = "flutua" if forca > 100 else "afunda"

    # Envia os resultados (ou None) para serem apresentados no template HTML.
    return render_template("index.html", forca=forca, estado=estado)


if __name__ == "__main__":
    # Executa a aplicação em modo debug para facilitar o desenvolvimento.
    app.run(debug=True)
