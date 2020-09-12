using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Challenges;
using System.Numerics;

namespace ChallengesTest
{
    [TestClass]
    public class PrimeTest
    {
        [TestMethod]
        public void SmallPrimes()
        {
            int[] numbers = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 };

            for (var i = 0; i < numbers.Length; i++)
            {
                Assert.IsTrue(Numbers.isPrime(numbers[i]));
            }

        }

        [TestMethod]
        public void Negatives()
        {
            int[] numbers = { -2, -3, -5, -7, -11, -13, -17, -19, -23, -29 };

            for (var i = 0; i < numbers.Length; i++)
            {
                Assert.IsFalse(Numbers.isPrime(numbers[i]));
            }
        }

        [TestMethod]
        public void PositiveNotPrime()
        {
            int[] numbers = { 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25 };

            for (var i = 0; i < numbers.Length; i++)
            {
                Assert.IsFalse(Numbers.isPrime(numbers[i]));
            }
        }

        [TestMethod]
        public void ZeroAndOne()
        {
            Assert.IsFalse(Numbers.isPrime(0));
            Assert.IsFalse(Numbers.isPrime(1));
        }

        [TestMethod]
        public void BigPrimes()
        {
            int[] numbers = {104677,104681, 104683, 104693, 104701, 104707, 104711, 104717, 104723, 104729 };

            for (var i = 0; i < numbers.Length; i++)
            {
                Assert.IsTrue(Numbers.isPrime(numbers[i]));
            }
        }
    }
}
