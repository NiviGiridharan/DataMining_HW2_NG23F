# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.27807

    level1["cough"] = -1.0
    level1["cough_info_gain"] = 0.03485

    level1["radon"] = -1.0
    level1["radon_info_gain"] = 0.23645

    level1["weight_loss"] = -1.0
    level1["weight_loss_info_gain"] = 0.02904

    level2_left["smoking"] = -1.0
    level2_left["smoking_info_gain"] = -1.0
    level2_right["smoking"] = -1.0
    level2_right["smoking_info_gain"] = -1.0

    level2_left["radon"] = -1.0
    level2_left["radon_info_gain"] = 0.07290
    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] = 0.72192

    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.72192
    level2_right["cough"] = -1.0
    level2_right["cough_info_gain"] = 0.32192

    level2_left["weight_loss"] = -1.0
    level2_left["weight_loss_info_gain"] = 0.17095
    level2_right["weight_loss"] = -1.0
    level2_right["weight_loss_info_gain"] = 0.17095
    

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    
    tree = u.BinaryTree("Tobacco Smoking")
    A = tree.insert_left("Chronic Cough")
    B = tree.insert_right("Radon Exposure")
    
    A.insert_left("Yes")
    A.insert_right("No")
    B.insert_left("Yes")
    B.insert_right("No")
    
    answer["tree"] = tree
    
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer

# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.4253
    # Infogain
    answer["(b) x < 0.2"] = 0.2147
    answer["(b) x < 0.7"] = 0.3739
    answer["(b) y < 0.6"] = 0.4979

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "y=0.6" 

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("y<=0.6")
    
    A = tree.insert_left("x<=0.7")
    A.insert_left("B")
    
    B = A.insert_right("y<=0.3")
    B.insert_left("A")
    B.insert_right("C")
    
    C = tree.insert_right("x<=0.2")
    C.insert_right("A")
    
    D = C.insert_left("y<=0.8")
    D.insert_left("C")
    D.insert_right("B")
    
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.1625
    answer["(e) Gini, Shirt type"] = 0.495

    answer["(f) attr for splitting"] = "Car type"

    # Explanatory text string
    answer["(f) explain choice"] = "Car type has the lowest gini index among the three attributes. Lowest gini index indicates a higher purity of classes with the subsets created by the split."

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ["Binary", "Qualitative", "Nominal"]
    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "Time expressed as AM or PM is a nominal qualitative feature because it has two separate categories and neither has an intrinsic order or numerical value."

    answer["b"] = ["Continuous", "Quantitative", "Ratio"]
    answer["b: explain"] = "Since brightness has a true zero (total darkness) and can fluctuate constantly, it is a ratio."

    answer["c"] = ["Discrete", "Quantitative", "Ordinal"]
    answer["c: explain"] = "Because people's perceptions of brightness may not be precisely quantified, they are qualitative in nature. Conversely, it can also be seen as ordinal since assessments can be ranked according to brightness."

    answer["d"] = ["Continuous", "Quantitative", "Ratio"]
    answer["d: explain"] = "Angles are quantitative attributes that are ratio-based since they are measured in degrees between 0 and 360, which depicts a continuous scale with a true zero point and equal intervals between measurements."

    answer["e"] = ["Binary", "Qualitative", "Ordinal"]
    answer["e: explain"] = "Medals awarded at the Olympics have a natural ordering (Bronze < Silver < Gold), making it an ordinal qualitative attribute. However, it is also binary since each medal can be considered as either won or not won."

    answer["f"] = ["Continuous", "Quantitative", "Interval"]
    answer["f: explain"] = "Height above sea level can theoretically take on any real value within a range, but it lacks a true zero point (sea level is an arbitrary reference point) and the intervals between measurements are uniform but arbitrary, making it an interval quantitative attribute."

    answer["g"] = ["Discrete", "Quantitative", "Ratio"]
    answer["g: explain"] = "The number of patients is countable with a true zero, making it ratio data."

    answer["h"] = ["Binary", "Qualitative", "Nominal"]
    answer["h: explain"] = "Books' ISBN numbers are nominal qualitative attributes that are essentially just a series of digits, letters, and hyphens that serve as unique identifiers without any numerical value or intrinsic order. Furthermore, every book is binary because it may be classified as having a legitimate ISBN or not."

    answer["i"] = ["Binary", "Qualitative", "Ordinal"]
    answer["i: explain"] = "The ability to pass light can be categorized into three distinct levels: opaque, translucent, and transparent, with a natural ordering (opaque < translucent < transparent), making it an ordinal qualitative attribute. However, it can also be considered binary since each material can be classified as either allowing light to pass through or not."

    answer["j"] = ["Discrete", "Qualitative", "Ordinal"]
    answer["j: explain"] = "Military rank consists of a finite set of distinct levels with a clear ordering, making it a discrete ordinal qualitative attribute."

    answer["k"] = ["Continuous", "Quantitative", "Ratio"]
    answer["k: explain"] = "Distance from the center of campus can take on any real value within a range, it has a true zero point and equal intervals between measurements, making it a continuous quantitative attribute with a ratio scale."

    answer["l"] = ["Continuous", "Quantitative", "Ratio"]
    answer["l: explain"] = "Density varies continuously, has a true zero, and measurements are directly comparable, making it ratio."

    answer["m"] = ["Discrete", "Qualitative", "Nominal"]
    answer["m: explain"] = "Coat check numbers are unique identifiers without quantitative value or order, representing nominal data."

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Even though Model 1's training accuracy is better, Model 2 has a higher test accuracy than Model 1. The Model 2 exhibits the least amount of variation in accuracy between training and testing. The best kind of model to use when predicting unknown data is this one."

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "Selecting Model 2 is preferable due to its consistent performance on newly discovered data, despite the fact that Model 1 has a higher accuracy on the combined dataset. Model 1 would appear to be the superior option if the accuracy of the combined dataset is the only consideration."

    explain["c similarity"] = "MDL and Pessimistic penalize complexity to avoid overfitting"
    explain["c similarity explain"] = "Both approaches penalize too complex models and choose models that strike a compromise between simplicity and accuracy in order to prevent overfitting."

    explain["c difference"] = "The appraoch to incorporate model complexity"
    explain["c difference explain"] = "Whereas pessimistic error estimation adjusts the error rate based on the size of the tree and accurate classifications, MDL employs a framework for data compression."

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = "x <= 0.5"
    answer["a, level 2, right"] ="A"
    answer["a, level 2, left"] = "y <= 0.4"
    answer["a, level 3, left"] = "A"
    answer["a, level 3, right"] = "x <= 0.2"
    
    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.58

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("x <= 0.5")

    A = tree.insert_right("A")
    B = tree.insert_left("y <= 0.4")
    
    B.insert_left("A")
    B.insert_right("x <= 0.2")
    
    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.531

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.2313
    answer["e, gain ratio, Handedness"] = 0.531

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

