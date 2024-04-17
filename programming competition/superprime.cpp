#include <iostream>

using namespace std;

/*---------------------------------------------------------------------Structs
*/
struct Node{
  int num;
  Node* next;
};

struct Queue{
  int len;
  Node* head;
  Node* tail;
};
/*---------------------------------------------------------------------Functions
*/
int int_exp(int number, int power){
  int counter=0;
  int value=1; //if power is 0 then value is 1... if power is 1 answer is number...etc
  while (counter<power){
    value= value*number;
    counter++;
  }
  return value;
}
/*---------------------------------------------------------------------
*/
void enqueue(Queue* &q, int data){
  //create and init Node for insert
  Node* n= new Node;
  n->num=data;
  n->next=NULL;
  //insert to list
  if (q->len==0){
    q->head=n;
    q->tail=n;
  }
  else{
    q->tail->next=n;
    q->tail=n;
  }
  q->len++;
  return;
}
/*---------------------------------------------------------------------
*/
int extract_digit(int target_digit, int source_number){
  int extraction;
  extraction= (source_number/(int_exp(10,target_digit-1)))%int_exp(10,target_digit);
  return extraction;
}
/*---------------------------------------------------------------------
*/
bool checkfactors(int number, int factor){
  bool isFactor=false;
  int test=number;

  test= test/factor;// testing to see if integer division
  test= test*factor;// and multiplication results in the smae number;
  if(test==number)
    isFactor=true;

  return isFactor;
}
/*---------------------------------------------------------------------
*/
bool test_prime(int number){
  int counter=2;
                            /*
                             -- !!! !! !!! this gave me cancer...
                             i usually initialize to 0... but doing
                              so would divide the number by 0 which
                               is not a thing... omg that took
                               forever to find... also everything
                               is divisiible by 1 so it would fuck
                               with the test.... !!!!!!!!!!!!!!
                               */
  bool isPrime=true;

  while (counter<number && isPrime==true){
    if(checkfactors(number, counter)){
      isPrime=false;
    }
    counter++;
  }
  return isPrime;
}
/*---------------------------------------------------------------------
*/
int num_length(int num){
  int length=0;
  while (num!=0){
    num=num/10;
    length++;
  }
  return length;
}
/*---------------------------------------------------------------------
*/
int main(){
  int top_range=0;
  int bot_range=0;
  int numlen=0;

  Queue* q=NULL;
  q= new Queue;
  //init q:
  q->len=0;
  q->head=NULL;
  q->tail=NULL;

  cout<<"\n\nnumbers for range 'low# high#'\n";
  scanf("%d %d",&bot_range, &top_range);// not sure why i used scanf here... must be familiarity with it over cin...
  int counter1= bot_range;
  int counter2=0;
  int digit=0;
  bool isSuperPrime=true;
  while(counter1<=top_range){
    if(test_prime(counter1)){
      numlen=num_length(counter1);
      while(counter2<numlen && isSuperPrime==true){
        digit= extract_digit(counter2,counter1);
        if (!test_prime(digit)){//!testprime is a double negative.. if prime it will return true.. this runs if the digit is not a prime (if test_prime returns false... !false == true)...
          isSuperPrime=false;
        }
        counter2++;
      }
      counter2=0;//reset fr next run
      if (isSuperPrime==true){
        //add the number to the queue
        enqueue(q, counter1);
      }
      else{
        isSuperPrime=true;// resets it for next run
      }
    }
    counter1++;
  }
  //print results from the program
  Node* tbd=q->head;//to be deleted
  Node* current=q->head;
  int print_counter=1;
  if (q->len!=0){
    cout << "\n" << q->len << " superprimes were found \n";
    while(current!= NULL){
      printf("\n%3d:\t\t\t%d", print_counter, current->num);
      //cout << "\n"<< print_counter << ": " << current->num;
      current=current->next;
      delete tbd;
      tbd= current;
      print_counter++;
    }
  }
  else{// q has nothing in it
    cout << "\n0 superprimes were found :(\n";
  }
  delete q;
  return 0;
}
