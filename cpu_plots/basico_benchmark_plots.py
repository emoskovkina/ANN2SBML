from matplotlib import pyplot as plt
import pickle
import statistics

with open('res.pickle', 'rb') as handle:
    res = pickle.load(handle)

encodings_chass = ["big_assignment_rules", "layers_as_compartments", "nodes_as_species", "nodes_as_parameters"]
encodings_pr = ["big_event_assignments", "layers_as_compartments", "nodes_as_species", "nodes_as_parameters"]
encodings = [encodings_chass, encodings_pr]
model_names_chass = ['original\nODE\nmodel'] + [f"FFNN.1.{i}" for i in range(1, 4)]
model_names_pr = ['original\nODE\nmodel'] + [f"ERNN.2.{i}" for i in range(1, 4)]
model_names = [model_names_chass, model_names_pr]

for case_study_res, model_names_case_study, encodings_case_study, case_study_name in zip(res, model_names, encodings, ("chass", "pr")):
    for encoding_res, encoding_name in zip(case_study_res, encodings_case_study):
        plt.figure(figsize=(9, 6), dpi=80)
        plt.boxplot(encoding_res)
        plt.xticks(range(1, len(encoding_res) + 1), model_names_case_study)
        ylim = plt.gca().get_ylim()
        delta_for_text_y = (ylim[1] - ylim[0])/100 # empiric value
        for i, el in enumerate(encoding_res):
            median = statistics.median(el)
            median_str = '%.2f' % median
            x = i+1.26
            y = median - delta_for_text_y
            plt.text(x, y, median_str)
        plt.ylabel("CPU (s)")

        plt.tight_layout()
        plt.savefig(f'{case_study_name}_{encoding_name}.png')
        plt.clf()

res2 = [[cs[0][0]] + [enc[1] for enc in cs] for cs in res]

encoding_names = ['original\nODE\nmodel', "encoding I", "encoding II", "encoding III", "encoding IV"]

for case_study_res, case_study_name in zip(res2, ("chass", "pr")):
    plt.figure(figsize=(9, 6), dpi=80)
    plt.boxplot(case_study_res)
    plt.xticks(range(1, len(case_study_res) + 1), encoding_names)
    ylim = plt.gca().get_ylim()
    delta_for_text_y = (ylim[1] - ylim[0])/100 # empiric value
    for i, el in enumerate(case_study_res):
        median = statistics.median(el)
        median_str = '%.2f' % median
        x = i+1.26
        y = median - delta_for_text_y
        plt.text(x, y, median_str)
    plt.ylabel("CPU (s)")

    plt.tight_layout()
    plt.savefig(f'{case_study_name}_smallest_different_encodings.png')
    plt.clf()

