abstract class Animal{

  void printName();
  void printSound();
}
class Cat extends Animal {
  @override 
  void printName(){
    print('The Animal Sound is CAt');
  }
  @override
  void printSound(){
    print('The Animal Sound is meoo');

  }
}
class Dog extends Animal {
  @override
  void printName(){
    print('The Animal Name is Dog');

  }
  @override
  void printSound(){
    print('The Animal Sound is yelp');
  }

}
class Cow extends Animal {
  @override
  void printName(){
    print('The Animal Name is Cow');
  }
  @override
  void printSound() {
    print('The Animal Sound is neigh');
  }
}
void main() {
  Cat ncat = Cat();
  ncat.printName();
  ncat.printSound();

  Dog ndog = Dog();
  ndog.printName();
  ndog.printSound();

  Cow ncow = Cow();
  ncow.printName();
  ncow.printSound();
}
