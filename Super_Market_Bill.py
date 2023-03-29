# #------------------Super Market Bill--------------------------

# itemp = {'Jam':30,'Bread':50,'Rice':175,'Dal':26.5,'Oil':20}
# oritem = []
# item = {1:'Jam',2:'Bread',3:'Rice',4:'Dal',5:'Oil'}
# i = 0
# print('List of items')
# print('1.Jam-Rs.30\n 2.Bread-Rs.50\n 3.Rice-Rs.175\n 4.Dal-Rs.26.5\n 5.Oil-Rs.20\n 6.Exit')
# print('Enter your choice 1 to 5 for purchase 6 for exit')
# t = int(input())
# while((t>=1)and(t<=5)):
#     i = i+1
#     print('Number of quantity required')
#     n=int(input())
#     t1 = item[t]     #extracts item name
#     t2 = itemp[t1]    #extracts price of an item
#     tc = n*t2
#     oritem = oritem+[item[t],itemp[t1],n,tc]
#     print('List of items')    
#     print('1.Jam-Rs.30\n 2.Bread-Rs.50\n 3.Rice-Rs.175\n 4.Dal-Rs.26.5\n 5.Oil-Rs.20\n 6.Exit')
#     print("Enter your choice 1 to 5 for purchase 6 for exit")
#     t = int(input())
# print("Retail Bill System")
# print('--------------------------------------------------------------------------')
# print('Name\t Price\t Quantity\t Total')
# print('--------------------------------------------------------------------------')
# ct = 0
# ind = 0
# for x in range(i):
#     print("%s\t%0.2f\t\t%d\t\t%0.2f"%(oritem[ind],oritem[ind+1],oritem[ind+2],oritem[ind+3]))
#     ct = ct+oritem[ind+3]
#     ind=ind+4
# print('----------------------------------------------------------------------------')
# print('Toal Amount %0.2f' %ct)