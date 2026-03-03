import time
import basico
from matplotlib import pyplot as plt
import pickle

original_model_path_chass = "../chassagnole1standard.xml"
original_model_path_pr = "../parkramstandard.xml"
original_model_pathes = [original_model_path_chass, original_model_path_pr]
nodes_chass = [[5, 5], [16, 16], [16, 16, 16]]
nodes_pr = [10, 15, 19]
encodings_chass = ["big_assignment_rules", "layers_as_compartments", "nodes_as_species", "nodes_as_parameters"]
encodings_pr = ["big_event_assignments", "layers_as_compartments", "nodes_as_species", "nodes_as_parameters"]
def get_nodes_str(nodes):
    return "_".join([str(el) for el in nodes])

plots_models_chass = [[f"../chass_different_encodings/chass_ffnn_tanh_{get_nodes_str(nod)}_{enc}_sbml.xml" for nod in nodes_chass] for enc in encodings_chass]
plots_models_pr = [[f"../pr_different_encodings/PR_ernn_relu_{nod}_{enc}_sbml.xml" for nod in nodes_pr] for enc in encodings_pr]
plots_models = [plots_models_chass, plots_models_pr]
res = [[[[] for _ in range(len(el) + 1)] for el in plots_models_case_study] for plots_models_case_study in plots_models]  

duration = 1000
for iteration in range(5):
    for i, (plots_models_case_study, original_model_path) in enumerate(zip(plots_models, original_model_pathes)):
        for j, el in enumerate(plots_models_case_study):
            fnames = [original_model_path] + el
            for k, fname in enumerate(fnames):
                step_number = duration
                start = time.time()

                model = basico.load_model(fname)
                df = basico.run_time_course(step_number=step_number, duration=duration)

                dif = time.time() - start
                print(iteration, duration, fname)
                res[i][j][k].append(dif)

with open('res.pickle', 'wb') as handle:
    pickle.dump(res, handle)