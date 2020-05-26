from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def eiwitvertalingen():
    """
    :return: Geeft de webpagina weer
    """
    seq = request.args.get("seq",'')
    # zorgt ervoor dat er grote en kleine letters kunnen worden
    # gebruikt.
    eiwit = translation(seq.lower())

    return render_template("eiwitvertalingen.html", seq=eiwit)

def translation(seq):
    """
    :param seq: De webpagina
    :return: De eiwitvertaling
    """
    code = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
            'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
            'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
            'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
            'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
            'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
            'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
            'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
            'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
            'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
            'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
            'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
            'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
            'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
            'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
            'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
            }
    try:
        if len(seq)==0:
            eiwit = "Geef een DNA sequentie "

        elif len(seq)/3 != float(len(seq)/3):
            eiwit = "Je hebt geen volledige sequentie opgegeven"
        else:
            dna = True
            for i in seq:
                if i not in ["a","t","g","c"]:
                    dna = False
                    eiwit = "Je hebt geen DNA opgegeven"

            if dna:
                try:
                    eiwit = ""
                    for i in range(0, len(seq), 3):
                        codon = seq[i:(i + 3)]
                        eiwit += code[codon]
                        if len(eiwit)//3:
                            print("Voer een sequentie is met de "
                                  "juiste hoeveelheid codons")
                        else:
                            pass
                except IndexError:
                    eiwit = "Geef een juiste DNA seqentie"
    except TypeError:
        eiwit = "Geef een DNA sequentie"
    return eiwit


if __name__ == '__main__':
    app.run()