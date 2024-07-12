from seleniumbase import BaseCase

class TestCase(BaseCase):

    # Function to fill left bowl with entered list
    def fill_left_bowl(self, bar_list=[]):
        for i in range(len(bar_list)):
            self.type(
                f'input[data-side="left"][data-index="{i}"]', bar_list[i]
            )
            self.sleep(0.2)

    # Function to fill right bowl with entered list
    def fill_right_bowl(self, bar_list=[]):
        for i in range(len(bar_list)):
            self.type(
                f'input[data-side="right"][data-index="{i}"]', bar_list[i]
            )
            self.sleep(0.2)

    # Function to split the lighter bowl in half to the left and right bowls
    def split_weights(self, result="", left_bowl=[], right_bowl=[]):
        print(f'Old Left Bowl: {left_bowl}')
        print(f'Old Right Bowl: {right_bowl}')
        print(len(left_bowl))
        print(left_bowl[:len(left_bowl)//2])
        print(left_bowl[len(left_bowl)//2:])
        # import ipdb; ipdb.set_trace()
        if "<" == result:
            return left_bowl[:len(left_bowl)//2], left_bowl[len(left_bowl)//2:]

        elif ">" == result:
            return right_bowl[:len(right_bowl)//2], right_bowl[len(right_bowl)//2:]
            right_bowl = right_bowl[len(right_bowl)//2:]

        print(f"New Left Bowl List: {left_bowl}")
        print(f"New Right Bowl List: {right_bowl}\n")

        return left_bowl, right_bowl

    def test_find_fake_gold_bar(self):
        answer = ""
        left_bowl = ['0','1','2','3']
        right_bowl = ['4','5','6','7']

        # Open exercise page
        self.open('http://sdetchallenge.fetch.com')
        self.wait_for_element('.game')

        # Initialize setup (split left bowl and right bowl with 4 numbers each)
        # Left bowl: [0, 1, 2, 3]
        self.fill_left_bowl(left_bowl)
        # Right bowl: [4, 5, 6, 7]
        self.fill_right_bowl(right_bowl)

        # Click the Weight button and assess results
        self.click('button#weigh')
        self.sleep(5)
        result = self.get_text('.result button#reset')
        self.assert_false("?" in result)
        print(f'Result: {result}\n')

        # If the bowls are equal, the fake bar is "8"
        if "=" == result:
            answer = "8"
            print(f'Gold Bar Number {answer} is the fake bar!')
            self.click('button#coin_8')
            self.sleep(2)
            return
        
        # Otherwise, split the lighter bowl into the two bowls
        left_bowl, right_bowl = self.split_weights(result, left_bowl, right_bowl)

        # Clear gameboard
        self.click('button#reset:not([disabled]')
        self.sleep(0.2)

        # Refill bowls with remaining bars from the lighter bowl
        self.fill_left_bowl(left_bowl)
        self.fill_right_bowl(right_bowl)

        # Repeat previous steps to check results and resplit the bowls
        self.click('button#weigh')
        self.sleep(5)
        result = self.get_text('.result button#reset')
        left_bowl, right_bowl = self.split_weights(result, left_bowl, right_bowl)
        self.click('button#reset:not([disabled]')
        self.sleep(0.2)
        self.fill_left_bowl(left_bowl)
        self.fill_right_bowl(right_bowl)

        # Down to 2 last bars, the lighter bowl is the answer
        self.click('button#weigh')
        self.sleep(5)
        result = self.get_text('.result button#reset')
        if "<" in result:
            answer = ''.join(left_bowl)
        elif ">" in result:
            answer = ''.join(right_bowl)
        print(f'Answer is Gold Bar Number {answer}')
        self.click(f'.coins > button#coin_{answer}')
        self.sleep(2)
        self.save_screenshot_to_logs(name='Fetch Challenge Result')
