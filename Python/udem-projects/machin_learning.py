from collections import defaultdict
import random

import language_tool_python

# Initialisiere LanguageTool für Deutsch
tool = language_tool_python.LanguageTool('de-DE')

# version 2
# class SimpleNGramModel:
#     def __init__(self, n):
#         self.n = n
#         # Ein Dictionary, um die n-grams zu speichern
#         self.ngrams = defaultdict(lambda: defaultdict(int))
#         # Ein Dictionary, um die Gesamtanzahl der Kontexte zu speichern
#         self.context_totals = defaultdict(int)
#
#
#     def train(self, text):
#         """Trainiert das Modell mit gegebenem Text."""
#         # Zerlegt den Text in Tokens (Wörter)
#         tokens = text.split()
#         # Erstellt n-grams und zählt deren Häufigkeiten
#         for i in range(len(tokens) - self.n + 1):
#             context = tuple(tokens[i:i + self.n - 1])  # Der Kontext sind die ersten n-1 Wörter
#             next_word = tokens[i + self.n - 1]  # Das vorherzusagende Wort ist das n-te Wort
#             self.ngrams[context][next_word] += 1
#             self.context_totals[context] += 1
#
#
#     def predict_next_word(self, context):
#         """Vorhersage des nächsten Wortes basierend auf dem gegebenen Kontext."""
#         context = tuple(context.split()[-(self.n - 1):])
#         # Prüft, ob der Kontext bekannt ist
#         if context in self.ngrams:
#             choices, weights = zip(*self.ngrams[context].items())
#             return random.choices(choices, weights=weights, k=1)[0]
#         else:
#             return "[Unbekannter Kontext]"
#
# # Beispieltext zum Trainieren des Modells
# text = "Hallo, wie geht es dir? Mir geht es gut. Und wie geht es dir? Es geht mir auch gut."
#
# # Ein 3-gram Modell erstellen und trainieren
# model = SimpleNGramModel(3)
# model.train(text)
#
# # Verschiedene Kontexte ausprobieren und das nächste Wort vorhersagen
# contexts = ["wie geht", "es dir", "geht es", "Hallo"]
#
# for context in contexts:
#     predicted_word = model.predict_next_word(context)
#     print(f"Kontext: '{context}' - Vorhergesagtes Wort: '{predicted_word}'")


# version 3


class EnhancedNGramModel:
    def __init__(self, n):
        self.n = n
        self.ngrams = defaultdict(lambda: defaultdict(int))
        self.context_totals = defaultdict(int)
        self.start_tokens = defaultdict(int)  # Zum Speichern der Starttoken für die Satzgenerierung
    
    
    def train(self, text):
        sentences = [s.strip() for s in text.split('.') if s]  # Zerlege den Text in Sätze
        for sentence in sentences:
            tokens = sentence.split()
            if len(tokens) < self.n:
                continue
            # Füge Starttokens hinzu, um die Satzgenerierung zu erleichtern
            self.start_tokens[tuple(tokens[:self.n - 1])] += 1
            for i in range(len(tokens) - self.n + 1):
                context = tuple(tokens[i:i + self.n - 1])
                next_word = tokens[i + self.n - 1]
                self.ngrams[context][next_word] += 1
                self.context_totals[context] += 1
    
    
    def predict_next_word(self, context):
        context = tuple(context.split()[-(self.n - 1):])
        if context in self.ngrams:
            choices, weights = zip(*self.ngrams[context].items())
            total = self.context_totals[context]
            probabilities = [weight / total for weight in weights]
            return random.choices(choices, weights=probabilities, k=1)[0]
        else:
            return "[Unbekannter Kontext]"
    
    
    def generate_sentence(self, start=None):
        if not start:
            start = random.choices(list(self.start_tokens.keys()), weights=self.start_tokens.values(), k=1)[0]
        current_context = start
        sentence = list(start)
        while True:
            next_word = self.predict_next_word(' '.join(current_context))
            if next_word == "[Unbekannter Kontext]" or len(sentence) > 100:  # Einfache Schleifen-/Längenbegrenzung
                break
            sentence.append(next_word)
            current_context = tuple(sentence[-(self.n - 1):])
        return ' '.join(sentence) + '.'

# Beispieltext zum Trainieren des Modells
text = "Hallo, wie geht es dir? Mir geht es gut. Und wie geht es dir? Es geht mir auch gut. Wie geht es dir heute?"

# Ein 3-gram Modell erstellen und trainieren
model = EnhancedNGramModel(3)
model.train(text)

# Generiere einen Satz mit einem gegebenen Startkontext
print("Generierter Satz mit Startkontext 'Wie geht':", model.generate_sentence("Wie geht"))

# Generiere einen Satz ohne spezifischen Startkontext
print("Generierter Satz ohne spezifischen Startkontext:", model.generate_sentence())

