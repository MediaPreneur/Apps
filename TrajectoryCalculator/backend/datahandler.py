

import datetime, os, random

class DataHandler:
    
    def __init__(self):
        user = os.getlogin()
        self.save_dir = 'C:/Users/USER/Desktop/trajectories'
        self.checkdir(self.save_dir)
    def random_name(self):
        now = datetime.datetime.now().strftime("%m%d%H%M%S")
        name = f'trajectory{now}.txt'
        
        return now
        
    def checkdir(self, dirr):
        if not os.path.isdir(dirr):
            try:
                os.makedirs(dirr)
            except:
                pass
    def checkfile(self,file):
        try:
            with open(file, 'r') as f:
            
                f.close()
                return True
        except:
            with open(file, 'w') as f:
                f.close()
    def save_trajectory_points(self, trajectory_points, name = ""):
        os.chdir(self.save_dir)
        name = self.random_name() if name == '' else f'{name}.txt'
        with open(name, 'w') as file:
            
            all_of_it = f"""[

        """
            for point in trajectory_points:
                all_of_it = f'{all_of_it}\n{point}'
            all_of_it = all_of_it + '\n]'
            file.write(all_of_it)
        print('trajectory saved')
    
    
    