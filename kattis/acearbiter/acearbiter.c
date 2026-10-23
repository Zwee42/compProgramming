#include <stdio.h>

void swap(int a[], int b[], int n) {
  for (size_t i = 0; i < n; i++) {
    int tmp = a[i];
    a[i] = b[i];
    b[i] = tmp;
  }
}

int main() {
  int n;
  scanf("%d", &n);
  int x[n];
  int y[n];

  for (int i = 0; i < n; i++) {
    scanf("%d-%d", &x[i], &y[i]);
  }

  if (n == 1) {
    if (x[0] == 11 && y[0] == 11) {
      printf("error 1\n");
      return 0;
    }
  }

  int last_round = 0;
  int round = 0;

  for (int i = 1; i < n; i++) {
    round = x[i - 1] + y[i - 1];
    int next_round = x[i] + y[i];
    int round_diff = next_round - round;
    int curX = x[i];
    int curY = y[i];
    int prevX = x[i - 1];
    int prevY = y[i - 1];
    int curSmall = curX < curY ? curX : curY;
    int prevSmall = prevX < prevY ? prevX : prevY;

    if (last_round > round) {
      printf("error %d\n", i);
      return 0;
    }

/*


*/

    // printf("Round %d: Score: %d:%d -> %d:%d\n", round + 1, prevX, prevY, curX,
    //        curY);

    // printf("Round %d\n", round);
    // printf("next round %d\n", next_round);

    // if (round > 1 && round % 2 && next_round % 2 == 0 &&
    //     (curX > prevX + round_diff || curY > prevY + round_diff)) {
    //   printf("error %d\n", i+1);
    //   return 0;
    // }

    last_round = round;

    if (prevX == 11 && prevY == 11) {
      printf("error %d\n", i);
      return 0;
    }

    // No score change
    if (curX == prevX && curY == prevY) {
      continue;
    }

    if (curX >= 11 && curY >= 11) {  // Game is over
      printf("error %d\n", i + 1);
      return 0;
    }


    if(curSmall < prevSmall){
      printf("error %d\n", i + 1);
      return 0;
    }

    if (round % 2) {
      if (curY >= 11 && (curX != prevX || curX >= 11)) {
        printf("err1or %d\n", i + 1);
        return 0;
      }
      if (curX >= 11 && ((curY != prevY) || curY >= 11)) {
        printf("er1ror %d\n", i + 1);
        return 0;
      }

      if (next_round % 2 == 0) {
        if (curX < prevX || curY < prevY) {
          printf("error %d\n", i );
          return 0;
        }
      } 
    } 
    else {
      if(next_round % 2 == 1 && round_diff % 2 == 1 && round_diff > 1){

        if(curX < prevX || curY < prevY){
          printf("error %d\n", i+1);
          return 0;
        }
      }
    }


    //A7 B9 round 16
    //A8 B9
    //B10 A8
    //B11 A8 round 19
    //NO

    //A7 B9 round 16
    //B10 A7 17
    //B10 A8 18
    //A8 B11 round 19
    // YES

    // FALSE A1 B23 A45 B67 A89 B1011 A1213 B1415 A1617 B1819 
    // TRUE A0 B12 A34 B56 A78 B910 A1112 B1314 A1516 B1718 A1920 B2122

    

    if (round % 2 == 0 && next_round % 2 == 1) {
      if(curX < prevY || curY < prevX){
        printf("error %d\n", i+1 );
        return 0;
      }
    }

    //  if (round > 3 && round % 2 && next_round % 2) {
    //   if(curX < prevY || curY < prevX){
    //     printf("error %d\n", i+1 );
    //     return 0;
    //   }
    // }



    if(prevX == curY && prevY == curX){
      printf("error %d\n", i + 1);
      return 0;
    }


  }
  round = x[n - 1] + y[n - 1];

  if (last_round > round) {
    printf("error %d\n", n);
    return 0;
  }
  printf("ok\n");
}
